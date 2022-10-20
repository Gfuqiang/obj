import logging
from loogers_demo.log_test_module import run_something

# logger = logging.basicConfig(filename='test_log.log', level=logging.DEBUG, filemode='w')

if __name__ == '__main__':

    # logging.debug('This is test to log debug level')
    # logging.debug('This is test to log info level')
    # run_something()
    print('start run')
    logg = logging.Logger('my_log')
    # logg = logging.getLogger('my_log')
    print(logg)
    print(logg.getEffectiveLevel())
    logg.info('This is one info log')
    logg.error('This is one error log')
    logg.debug('This is one debug log')