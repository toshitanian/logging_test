import logging
import sys
def setup_logging():
    stream_log = logging.StreamHandler(sys.stdout)
    stream_log.setLevel(logging.INFO)
    stream_log.setFormatter(
        logging.Formatter(
            'time:%(asctime)s\tlevel:%(levelname)s\tmethod:%(funcName)s\tlineno:%(lineno)d\t%(message)s'
        )
    )
    default_logger = logging.getLogger('default')
    default_logger.setLevel(logging.INFO)
    default_logger.addHandler(stream_log)

    return default_logger
