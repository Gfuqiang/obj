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

# start_time = "2022-05-28"
# end_time = "2022-06-12"
#
# start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d')
# end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')
#
# res_time = end_time - start_time
# for i in range(res_time.days):
#     start_time = start_time + datetime.timedelta(days=1)
#     print(datetime.datetime.strftime(start_time, '%Y-%m-%d'))





