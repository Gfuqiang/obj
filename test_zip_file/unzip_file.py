import os,zipfile


def unzip(zip_path, unzip_path):
    if not os.path.exists(unzip_path):
        os.mkdir(unzip_path)
    z = zipfile.ZipFile(zip_path, 'r', compression=zipfile.ZIP_DEFLATED)
    for file in z.namelist():
        z.extract(file, unzip_path)
    z.close()


if __name__ == '__main__':
    unzip('./zip_dir/test.zip', './unzip_dir')