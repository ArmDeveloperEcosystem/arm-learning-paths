---
title: Demo - Run kubectl on Arm CPU
overview: Kubernetes supports many types of apps - web/game servers, data storage, AI training/inference, and so much more. It also supports many architectures, including Arm64. Using this Arm Kubernetes migration tool, you can identify if your cluster already just works on arm64. This demo illustrates how easy it is to run this tool yourself by using pre-loaded Kubernetes cluster config files and a console notebook to run the tool within.

demo_steps:
  - Select a Kubernetes cluster file to analyze.
  - Run the Kubernetes migration tool in the demo space.
  - Review the output and stats to understand it.

diagram: kubernetes_diagram.png

configuration_popup_details: Super long list of configuration information to provide to the user. Should be context and all that to be crystal clear what the setup is.

configuration_dropdown_options:
  - parameters:
      param_name: Cluster .yaml file
      options:
        - name: Hosted LLM chatbot
          specs: Hosted LLM chatbot cluster includes Rancher packages, the web server NGINX, Redis, and Mongo-DB as a simple database. ML capabilities come from TensorFlow and Rocket.chat modules.
        - name: other file
          specs: Other information.
      selectable: true
      explanation: Helpbox info that isn't used yet.


### Specific details to this demo
# ================================================================================
prismjs: true

### FIXED, DO NOT MODIFY
# ================================================================================
demo_template_name: kubectl_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
