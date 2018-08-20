import logging


def init_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S',
                        )
    return logging.getLogger()


logger = init_logger()
