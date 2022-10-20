import os
import zipfile, pathlib

dir_path = pathlib.Path('.')
file_path = dir_path / 'zip_file_dir' / 'job-export-2022-06-21-09_46_42-1'
zip_dir_path = dir_path / 'zip_file_dir' / 'zip_file.zip'

f = zipfile.ZipFile(zip_dir_path, 'w', compression=zipfile.ZIP_LZMA)
for root, dirs, files in os.walk(file_path):
    dir_path = root.replace(str(file_path), '') and root.replace(str(file_path), '') + os.sep or ''
    for file in files:
        f.write(os.path.join(root, file), dir_path + file)
f.close()

