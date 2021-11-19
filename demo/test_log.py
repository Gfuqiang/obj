import logging
from logging import config


def advance():
    # Logger 记录器
    logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO)

    logFormat = logging.Formatter("%(message)s")

    stream = logging.StreamHandler()
    stream.setFormatter(logFormat)
    logger.addHandler(stream)

    logger.info('ni hao')


def log_record():
    # record = logging.LogRecord('me', 'INFO', 'me.log', 1, )
    record = logging.makeLogRecord({
        'name': 'me',
        'level': 'INFO',
        'pathname': 'me.log',
        'msg': 'This is msg'
    })
    print(record.filename)


def main():
    import time

    class MyFormatter(logging.Formatter):
        converter = time.gmtime()
        default_time_format = '%Y-%m-%d %H:%M:%S'
        default_msec_format = '%s,%03d'
        def __init__(self, fmt=None):
            super(MyFormatter, self).__init__(fmt=None, datefmt=None, style='%')

    for_matter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    for_mymatter = MyFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    print(dir(for_matter))
    print(dir(for_mymatter))
    # logging 基础用法
    # logging.basicConfig(filename='myapp.log', level=logging.INFO)
    # 进阶用法
    loggerr = logging.getLogger(__name__)
    loggerr.setLevel(logging.INFO)

    str_handler = logging.StreamHandler()
    str_handler.setFormatter(for_matter)
    mystr_handler = logging.StreamHandler()
    mystr_handler.setFormatter((for_mymatter))
    loggerr.addHandler(str_handler)
    loggerr.addHandler(mystr_handler)

    loggerr.info('Started')
    print('Do something')
    loggerr.error('Finished')


def log_dict_conf():
    dict_data = {
        'version': 1,
        'formatters': {
            'format_1': {
                'format': 111
            }
        }
    }
    config.dictConfig()

def version():
    VERSION = (2, 2, 0, 'final', 0)

    __version__ = VERSION
    print(__version__)

if __name__ == '__main__':
    # log_record()

    version()
