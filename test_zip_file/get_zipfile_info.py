import zipfile

if __name__ == '__main__':
    with zipfile.ZipFile('./zip_dir/test.zip') as z:
        z.infolist()

    print(zipfile.ZipFile('./zip_dir/test.zip').infolist())

