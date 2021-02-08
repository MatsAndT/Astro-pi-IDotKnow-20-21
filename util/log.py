import logging
import traceback
from typing import Callable

_formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s: (%(name)s) %(message)s')

try:
    os.mkdir(os.path.join('output'))
except FileExistsError:
    pass

_filehandler = logging.FileHandler('output/output.log')
_filehandler.setFormatter(_formatter)
_filehandler.setLevel(logging.INFO)

_level = logging.INFO


def set_level(level: int):
    global _level
    _level = level


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(_formatter)
    stream_handler.setLevel(_level)
    logger.addHandler(stream_handler)

    logger.addHandler(_filehandler)

    return logger


def log_func(logger: logging.Logger = None) -> Callable:
    """
    Logs function calls, return values, and exceptions, of decorated function.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    def decorator(func):
        def log_func_wrapped(*args, **kwargs):
            logger.debug(f"Calling func {func}, with args {args}, and kwargs {kwargs}.")
            try:
                retval = func(*args, **kwargs)
                logger.debug(f"Function {func} returned value {retval}.")
                return retval
            except:
                logger.error(f"Function {func} raised exception:\n{traceback.format_exc()}")
                raise

        return log_func_wrapped

    return decorator
