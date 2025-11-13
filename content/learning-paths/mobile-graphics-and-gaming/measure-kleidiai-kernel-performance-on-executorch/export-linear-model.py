
import torch
import torch.nn as nn

class DemoLinearModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256,256)

    def forward(self, x):
        y = self.linear(x)
        return y

    def get_example_inputs(self,dtype=torch.float32):
        return (torch.randn(1, 256, dtype=dtype),)


from executorch.backends.xnnpack.partition.xnnpack_partitioner import XnnpackPartitioner
from executorch.backends.xnnpack.partition.config.xnnpack_config import ConfigPrecisionType
from executorch.exir import to_edge_transform_and_lower

def export_executorch_model(dtype: torch.dtype, model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"
    
    model = DemoLinearModel().eval().to(dtype)
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

export_executorch_model(torch.float16,"linear_model_pf16_gemm")
export_executorch_model(torch.float32,"linear_model_pf32_gemm")


from torchao.quantization.pt2e.quantize_pt2e import convert_pt2e, prepare_pt2e
from executorch.backends.xnnpack.quantizer.xnnpack_quantizer import (
    get_symmetric_quantization_config,
    XNNPACKQuantizer,
)

def export_int8_quantize_model(dynamic: bool, model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"
    
    model = DemoLinearModel().eval().to(torch.float32)
    example_inputs = model.get_example_inputs(torch.float32)
    
    #Quantizer model 
    model = torch.export.export(model, example_inputs).module()
    quantizer = XNNPACKQuantizer()
    operator_config = get_symmetric_quantization_config(
        is_per_channel=True,
        is_dynamic=dynamic
    )

    quantizer.set_global(operator_config)
    quantize_model = prepare_pt2e(model, quantizer)
    quantize_model(*example_inputs)
    quantize_model = convert_pt2e(quantize_model)

    #export model
    exported_program = torch.export.export(quantize_model, example_inputs)
    
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

export_int8_quantize_model(False,"linear_model_pqs8_qc8w_gemm");
export_int8_quantize_model(True,"linear_model_qp8_f32_qc8w_gemm");


from torchao.quantization.granularity import PerGroup, PerAxis
from torchao.quantization.quant_api import (
    IntxWeightOnlyConfig,
    Int8DynamicActivationIntxWeightConfig,
    quantize_,
)

def export_int4_quantize_model(dynamic: bool, model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"
    
    model = DemoLinearModel().eval().to(torch.float32)
    example_inputs = model.get_example_inputs(torch.float32)
    
    #Quantizer model 

    linear_config = Int8DynamicActivationIntxWeightConfig(
        weight_dtype=torch.int4,
        weight_granularity=PerGroup(32),
    )

    quantize_(model, linear_config)

    #export model
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

export_int4_quantize_model(False,"linear_model_qp8_f32_qb4w_gemm");



