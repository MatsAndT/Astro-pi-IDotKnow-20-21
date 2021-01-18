import os
import time

from util.log import log_func, get_logger

logger = get_logger(__name__)

_imgsize_cache = dict()
_max_size = 2.9 * 10 ** 9  # 2.9GB


def get_size(path: str):
    if not os.path.isdir(path):
        return None

    files = [os.path.join(path, file) for file in os.listdir(path)]
    filesizes = dict()

    for file in files:
        if not os.path.isfile(file):
            continue

        if not file.endswith('.jpg'):
            continue

        if file in _imgsize_cache.keys():
            continue

        filesizes[file] = os.path.getsize(file)

    _imgsize_cache.update(filesizes)

    return sum(_imgsize_cache.values())


@log_func(logger)
def is_space_left(self, path: str):
    if get_size(path) >= _max_size:
        logger.info("Storage not available")
        return False
    else:
        logger.info("Storage available")
        return True
