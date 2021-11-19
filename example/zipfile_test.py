import zipfile

print(zipfile.is_zipfile('job-285435d1-dcd5-9116-af8a-25857f5989f3.zip'))
with zipfile.ZipFile('shell_returen.py.zip', 'r') as z:
    print(type(z))
    print(type(z.getinfo('shell_returen.py')))
    d = z.testzip()
    print(z.namelist())
    for info in z.namelist():
        print(type(info))
    print(d)
    # data = z.testzip()
    # print(data)


zip_info = zipfile.ZipInfo('job-285435d1-dcd5-9116-af8a-25857f5989f3.zip')
# print(zip_info)



