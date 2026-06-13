import sys

try:
    import torch
except ModuleNotFoundError:
    print('ERROR: torch is not installed in this environment.')
    sys.exit(1)

print('Python:', sys.version.split()[0])
print('Torch:', torch.__version__)
print('CUDA available:', torch.cuda.is_available())
print('CUDA device count:', torch.cuda.device_count())

if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f'Device {i}:', torch.cuda.get_device_name(i))
    print('Current CUDA device:', torch.cuda.current_device())
else:
    print('No CUDA-enabled GPU detected.')
