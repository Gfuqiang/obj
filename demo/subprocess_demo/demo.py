import subprocess, os, datetime
from pathlib import Path


p = Path(".")
q = p / "media" / "empty"

if not q.exists():
    q.mkdir()



# find ./ -maxdepth 1 -type d -name "2022_05_1*"|xargs -i rsync --delete-before -av empty/ {}
dir_name = "2022_05_01"
complete_process = subprocess.run(
    'find ./media -maxdepth 1 -type d -name "2022_05_01" | xargs -I {} rsync --delete-before -av media/empty/ {}',
    shell=True
)
print(complete_process)





