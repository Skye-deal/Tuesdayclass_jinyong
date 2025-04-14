import torch
print(torch.cuda.is_available())  # Check if CUDA is available
print(torch.cuda.current_device())  # Get the current device index

import torch

if torch.cuda.is_available():
    print("GPU is available!")
    print(f"Current device index: {torch.cuda.current_device()}")
    print(f"Device name: {torch.cuda.get_device_name(torch.cuda.current_device())}")
else:
    print("GPU is not available.")