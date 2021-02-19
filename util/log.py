import logging
import traceback
from typing import Callable
import os

# Logging formatter
_formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s: (%(name)s) %(message)s')

# Make sure output directory exists.
try:
    os.mkdir(os.path.join('output'))
except FileExistsError:
    pass

_level = logging.INFO

# Logging handlers
_filehandler = logging.FileHandler('output/output.log')
_filehandler.setFormatter(_formatter)
_filehandler.setLevel(logging.INFO)

_stream_handler = logging.StreamHandler()
_stream_handler.setFormatter(_formatter)
_stream_handler.setLevel(_level)




def set_level(level: int):
    """Global logging level setter"""
    global _level
    _level = level


def get_logger(name: str) -> logging.Logger:
    """Get logger and add default handlers if necessary"""
    logger = logging.getLogger(name)

    _stream_handler.setLevel(_level)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)

    logger.addHandler(_stream_handler)
    logger.addHandler(_filehandler)

    return logger


def log_func(logger: logging.Logger = None) -> Callable:
    """
    Logs function calls, return values, and exceptions, of decorated function.
    For testing and debugging purposes.
    """
    if logger is None:
        logger = get_logger('astro')

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
