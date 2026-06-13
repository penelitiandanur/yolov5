import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent
config_file = base_dir / 'auto_config.json'

def main():
    config = {
        'project': 'yolov5',
        'environment': str(base_dir / 'venv'),
        'python': 'venv\\Scripts\\python.exe',
        'requirements': 'requirements.txt',
        'cuda_required': True,
        'torch_required': 'torch>=1.8.0',
        'torchvision_required': 'torchvision>=0.9.0'
    }

    with config_file.open('w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)

    print('Auto configuration file created at:', config_file)
    print('Run this script or use the generated config for setup automation.')

if __name__ == '__main__':
    main()
