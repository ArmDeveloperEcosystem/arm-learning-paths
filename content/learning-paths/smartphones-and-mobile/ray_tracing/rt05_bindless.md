---
title: "Bindless materials"
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Bindless materials

Bindless resources are implemented by `VK_EXT_descriptor_indexing` and have been a core feature of Vulkan since version 1.2. It is independent of ray tracing, and technically it is possible to implement ray tracing effects without using it, however it makes it easy and simple to access the data of the intercepted objects.

Descriptor Indexing allows applications to define arrays of buffers and textures that shaders can access using dynamic and non-uniform indices. This extension then enables you to keep all your resources organized in look-up tables.

In a traditional rasterized renderer, applications bind all the necessary information of an object to each draw call, allowing you to retrieve the material, position, and texture that is needed to draw it. However, when you use ray tracing, this approach will not enable you to identify the materials of the hit object. Instead, you must use a unique identifier to retrieve the necessary information from look-up tables.

The ray query API allows you to obtain an instance ID, a geometry ID, and a primitive ID from the acceleration structure that you can use to query these tables.

``` glsl
#extension GL_EXT_ray_query : require

uint intersection_custom_instance_id = rayQueryGetIntersectionInstanceCustomIndexEXT(rayQuery, committed_intersection);
uint intersection_geometry_id = rayQueryGetIntersectionGeometryIndexEXT(rayQuery, committed_intersection);
uint intersection_primitive_id = rayQueryGetIntersectionPrimitiveIndexEXT(rayQuery, committed_intersection);
uint intersection_geometry_global_index = intersection_custom_instance_id + intersection_geometry_id;
```

As you build the acceleration structure, you can keep track of how many geometries each instance contains, and make sure that everything can be identified uniquely using the sum of the instance custom ID and the geometry ID. You can build a set of look-up tables so that with this unique identifier you can access everything that you need to render the intersected triangle:

``` cpp
uint32_t custom_index = 0;
for (const auto &scene_blas : get_scene_blases())
{
    // Assign a unique id to each BLAS in our scene
    scene_blas->custom_index = custom_index++;
    assert(custom_index < (1 << 24) && "Instance custom index overflow");
    custom_index += scene_blas.get_geometry_children().size();

    // Set the unique id as instanceCustomIndex
    VkAccelerationStructureInstanceKHR child_instance{};
    child_instance.instanceCustomIndex = to_u32(scene_blas->custom_index);
}
```

With the Primitive ID you can access the relevant index buffer and retrieve all the vertex attributes, including texture coordinates. The API also provides the barycentric coordinates of the intersection point. Using this, you can mimic a `Fragment` shader and interpolate the attributes, for example the UV coordinates.

``` glsl
#extension GL_EXT_nonuniform_qualifier : require

layout(set = BINDLESS_MESHES_SET, binding = 0, scalar) readonly buffer Mesh_texcoord_Buffer
{
    vec2 texcoord[];
}
mesh_texcoord[BINDLESS_MAX_MESHES];

layout(set = BINDLESS_MESHES_SET, binding = 1, scalar) readonly buffer Mesh_indices_Buffer
{
    vec2 indices[];
}
mesh_indices[BINDLESS_MAX_MESHES];

layout(set = BINDLESS_DRAWABLES_SET, binding = 2, scalar) readonly buffer BindlessKeysBuffer
{
    uint per_geometry[];
}
bindless_keys;

vec2 bary_lerp(vec2 a, vec2 b, vec2 c, vec3 barycentrics)
{
    return a * barycentrics.x + b * barycentrics.y + c * barycentrics.z;
}

vec3 bary_lerp(vec3 a, vec3 b, vec3 c, vec3 barycentrics)
{
    return a * barycentrics.x + b * barycentrics.y + c * barycentrics.z;
}

ivec3 get_indices(uint mesh_id, uint primitive_id)
{
    return ivec3(mesh_indices[nonuniformEXT(mesh_id)].indices[3 * primitive_id + 0],
                 mesh_indices[nonuniformEXT(mesh_id)].indices[3 * primitive_id + 1],
                 mesh_indices[nonuniformEXT(mesh_id)].indices[3 * primitive_id + 2]);
}

vec2 get_intersection_uv(uint bindless_key, vec2 barycentrics, uint primitive_id)
{
    uint mesh_id = (bindless_key >> 8) & 0xFFF;
    uint material_id = bindless_key & 0xFF;

    ivec3 ind = get_indices(mesh_id, primitive_id);

    vec2 uv0 = mesh_texcoord[nonuniformEXT(mesh_id)].texcoord[ind.x];
    vec2 uv1 = mesh_texcoord[nonuniformEXT(mesh_id)].texcoord[ind.y];
    vec2 uv2 = mesh_texcoord[nonuniformEXT(mesh_id)].texcoord[ind.z];

    vec2 uv = bary_lerp(uv0, uv1, uv2, vec3(1.0 - barycentrics.x - barycentrics.y, barycentrics.x, barycentrics.y));
    return uv;
}

vec2 get_intersection_uv(in rayQueryEXT rayQuery)
{
    const bool committed_intersection = true;
    vec2 barycentrics = rayQueryGetIntersectionBarycentricsEXT(rayQuery, committed_intersection);
    uint custom_instance_id = rayQueryGetIntersectionInstanceCustomIndexEXT(rayQuery, committed_intersection);
    uint geometry_id = rayQueryGetIntersectionGeometryIndexEXT(rayQuery, committed_intersection);
    uint primitive_id = rayQueryGetIntersectionPrimitiveIndexEXT(rayQuery, committed_intersection);

    uint geometry_global_index = custom_instance_id + geometry_id;
    uint bindless_key = bindless_keys.per_geometry[geometry_global_index];

    return get_intersection_uv(bindless_key, barycentrics, primitive_id);
}
```

Note that to optimize memory consumption, you have compressed the mesh and material identifier in a single `uint`.

Once you have our UV coordinates, you can retrieve the material ID from a different table and use it to index into our texture arrays. You also keep separate bindless arrays, each one containing the different textures you will need to use. Finally, you can then use the UV coordinates to sample the textures and compute the final color.

``` glsl
layout(set = BINDLESS_MATERIALS_SET, binding = binding_index) uniform texture2D base_color_textures[BINDLESS_MAX_MATERIALS];

layout(set = BINDLESS_MATERIALS_SET, binding = 0) uniform sampler texture_sampler;

vec4 get_bindless_base_color(uint material_id, vec2 uv, uint texture_mip)
{
    return textureLod(sampler2D(base_color_textures[nonuniformEXT(material_id)], texture_sampler), uv, intersection_mip).rgba;
}

vec4 get_bindless_base_color(in rayQueryEXT rayQuery)
{
    const bool committed_intersection = true;
    vec2 barycentrics = rayQueryGetIntersectionBarycentricsEXT(rayQuery, committed_intersection);
    uint custom_instance_id = rayQueryGetIntersectionInstanceCustomIndexEXT(rayQuery, committed_intersection);
    uint geometry_id = rayQueryGetIntersectionGeometryIndexEXT(rayQuery, committed_intersection);
    uint primitive_id = rayQueryGetIntersectionPrimitiveIndexEXT(rayQuery, committed_intersection);

    uint bindless_key = bindless_keys.per_geometry[geometry_global_index];

    uint intersection_mip = 0;
    vec2 uv = get_intersection_uv(bindless_key, barycentrics, primitive_id);
    uint mesh_id = (bindless_key >> 8) & 0xFFF;
    uint material_id = bindless_key & 0xFF;
    vec4 base_color = get_bindless_base_color(material_id, uv, texture_mip);
    return base_color;
}
```