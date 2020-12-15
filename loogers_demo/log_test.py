import logging
from loogers_demo.log_test_module import run_something

logger = logging.basicConfig(filename='test_log.log', level=logging.DEBUG, filemode='w')

if __name__ == '__main__':

    logging.debug('This is test to log debug level')
    logging.debug('This is test to log info level')
    run_something()