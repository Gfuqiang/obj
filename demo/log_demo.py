import logging


def main():
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger('my_log')
    logger.warning(f'This is a warning')


if __name__ == '__main__':
    main()
