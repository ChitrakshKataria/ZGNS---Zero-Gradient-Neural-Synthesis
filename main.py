import torch


### Device Agnostic code
def GetDevice(forceCPU=False):
    if forceCPU:
        device = torch.device("cuda")
        device_name = "CPU"
        return device, device_name
    if torch.cuda.is_available():
        device = torch.device("cuda")
        device_name = torch.cuda.get_device_name(0)
        return device, device_name
    if torch.backends.mps.is_available():
        device = torch.device("mps")
        device_name = "Metal MPS"
        return device, device_name
    try:
        import torch_directml

        if torch_directml.device_count() > 0:
            device = torch_directml.device()
            device_name = torch_directml.device_name(0)
            return device, device_name
    except ImportError:
        pass


device = GetDevice(forceCPU=False)
print(device)
