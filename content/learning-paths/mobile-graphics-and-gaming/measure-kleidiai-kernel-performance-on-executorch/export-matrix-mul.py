
import torch
import torch.nn as nn

class DemoBatchMatMulModel(nn.Module):
    def forward(self, x,y):
        return torch.bmm(x, y)  

    def get_example_inputs(self,dtype=torch.float32): 
        return (torch.randn(1, 256, 256, dtype=dtype),torch.randn(1, 256, 256, dtype=dtype))


from executorch.backends.xnnpack.partition.xnnpack_partitioner import XnnpackPartitioner
from executorch.backends.xnnpack.partition.config.xnnpack_config import ConfigPrecisionType
from executorch.exir import to_edge_transform_and_lower

def export_mutrix_mul_model(dtype: torch.dtype, model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"
    
    model = DemoBatchMatMulModel().eval().to(dtype)
    example_inputs = model.get_example_inputs(dtype)
    
    exported_program = torch.export.export(model, example_inputs)
    
    partitioner = XnnpackPartitioner()
    edge_program = to_edge_transform_and_lower(
        exported_program,
        partitioner=[partitioner],
        generate_etrecord=True
    )
    
    et_program = edge_program.to_executorch()
    with open(pte_file, "wb") as f:
        f.write(et_program.buffer)
    
    # Get and save ETRecord
    etrecord = et_program.get_etrecord()
    etrecord.save(etr_file)

export_mutrix_mul_model(torch.float16,"matrix_mul_pf16_gemm")
export_mutrix_mul_model(torch.float32,"matrix_mul_pf32_gemm")

