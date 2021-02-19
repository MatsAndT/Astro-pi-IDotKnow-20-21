import os
import time

from util.log import log_func, get_logger

logger = get_logger('astro')

_imgsize_cache = dict()
_max_size = 2.9 * 10 ** 9  # 2.9GiB


def get_size(path: str):
    """Gets total size of files in path"""
    if not os.path.isdir(path):
        return None

    filesizes = dict()

    for root, dirs, files in os.walk(path):
        for file in files:
            file = os.path.join(root, file)
            if not os.path.isfile(file):
                continue

            # Only check images
            if not file.endswith('.jpg'):
                continue

            # Only check file size if we haven't checked it already.
            if file in _imgsize_cache.keys():
                continue

            filesizes[file] = os.path.getsize(file)

    _imgsize_cache.update(filesizes)

    return sum(_imgsize_cache.values())


@log_func(logger)
def is_space_left(path: str):
    """Check if there is enough space for the experiment to continue."""
    usage = get_size(path)
    if usage >= _max_size:
        logger.info("Storage not available")
        return False
    else:
        logger.info(f"Storage available, {usage}/{_max_size}")
        return True
