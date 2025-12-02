import torch
print("CUDA доступна:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("✅ Пристрій:", torch.cuda.get_device_name(0))
    print("Версія CUDA в Torch:", torch.version.cuda)
    print("Torch build:", torch.__version__)
