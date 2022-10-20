import os,sys
from distutils.core import setup
from Cython.Build import cythonize

dir_paths = ['apiv1']


files = [i + '/*.py' for i in dir_paths]

if 'build_ext' in sys.argv:
    setup(ext_modules=cythonize(['apiv1/util.py'], exclude=['__init__.py']))
else:
    for item in dir_paths:
        for dirpath, foldernames, filenames in os.walk(item):
            for file in filenames:
                if dirpath == item + '/migrations':
                    break
                if (file.endswith('.py') or file.endswith('.c') or file.endswith('.pyc')):
                    os.remove(dirpath + '/' + file)