""""
contextmanager 装饰器，将函数变为上下文管理器
"""
import logging
from contextlib import contextmanager


@contextmanager
def custom_logger_level(level, log_name):
    logger = logging.getLogger(log_name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


if __name__ == '__main__':
    # 下一下内容不会打印，因为log默认基本是error
    logging.debug(f'error message')
    with custom_logger_level(logging.DEBUG, 'my_log') as logger:
        print(logger.getEffectiveLevel())
        print(logger)
        # logger 在上下文管理器中level被设置为debug
        logger.debug(f'This is debug message')
        logging.debug(f'This is debug message two')

