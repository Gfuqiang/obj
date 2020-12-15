import zipfile

if __name__ == '__main__':
    zipfile_info = zipfile.ZipInfo('./zip_dir/test.zip')
    print(zipfile_info)