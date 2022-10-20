import sys
import zipfile, pathlib

from demo import list_cut

_NEEDS_LOADING = object()


class A:

    pass

if __name__ == '__main__':
    name = 'django.contrib.admin'
    # for k, v in sys.modules.items():
    #     # print(f'{k}: {v}')
    #     # print(type(k), type(v))
    #     # break
    #     cls = getattr(v, k, None)
    #
    #     if cls:
    #         print(type(cls))
    #         print(f'{k}: {v}')
    # print(issubclass(cls, A))
    p = pathlib.Path('.')
    p = p / '压测用例_innerjob.zip'
    unzip_path = pathlib.Path('.')
    unzip_path = unzip_path / 'unzip_dir'
    with zipfile.ZipFile(p, 'r') as zf:
        zf.extractall(unzip_path)

    # module = sys.modules.get(name, _NEEDS_LOADING)