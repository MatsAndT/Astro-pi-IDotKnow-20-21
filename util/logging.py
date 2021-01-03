import logging
import traceback

formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s: (%(name)s) %(message)s', )

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)


def log_func(logger: logging.Logger = None):
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
