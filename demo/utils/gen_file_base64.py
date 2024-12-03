import base64
import io
import pathlib
from tempfile import TemporaryFile


def read_file_base64():
    path = pathlib.Path(__file__).parent.parent.absolute()
    file_path = path.joinpath('resouce_files', '截图照片.png')
    with open(file_path, "rb") as f:
        # return base64.b64encode(f.read()).decode("utf-8")
        while content := f.read(1024):
            print(content)

class ClassPropertyChange:

    def __init__(self):
        self.name = None


    def call_func(self, data):
        self.data = data
        return self.get_data()

    def get_data(self):
        return {"data": self.data}

if __name__ == '__main__':
    print(isinstance(TemporaryFile, io.BytesIO))
    # base64 = read_file_base64()
    # print(base64)

    prop_change = ClassPropertyChange()
    ret = []
    for i in range(10):
        ret.append(prop_change.call_func(i))
    print(ret)
