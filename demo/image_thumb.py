import os

import cv2
from PIL import Image
from pathlib import Path, PurePath


if __name__ == '__main__':
    # p1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # p2 = Path(p1 + os.sep + 'demo' + os.sep + 'test.py')
    # # demo = os.path.join(p2, 'demo', 'demo1.py')
    # print(p2.exists())
    # print(p2.is_file())
    # print(p2.unlink())
    # print(p2)
    # print(type(p2))

    # p = Path('flow_8035_inner_2_1_3ocr-0.70240.png')
    # image = Image.open(p)
    src = cv2.imread('/Users/fq/Desktop/work/obj/demo/flow_8035_inner_2_1_3ocr-0.70240.png')
    # width, height = image.size
    # print(f'width: {width}')
    # print(f'height: {height}')
    # new_width = int(width * 1.0 / 2)
    # print(f'new width: {new_width}')
    # image.thumbnail((150, new_width))
    # p1 = PurePath()
    # path = os.path.join(str(p1), 'test.png')
    # image.save(path)
    print(src.shape)





