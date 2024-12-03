from pathlib import Path

path = Path('demo1.py')
path = path.resolve(strict=True)

print(str(path))
print(type(path))