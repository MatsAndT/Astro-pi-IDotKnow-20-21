from util.logging import log_func, get_logger
import os
from time import sleep

logger = get_logger(__name__)

class Space:
    total_image_data_size = 0

    @log_func(logger)
    def add_size(self, id):
        try:
            img_size = os.path.getsize(f"{self.img_path}{id}.jpg")
            logger.debug(f"img_size: {img_size}")
        except FileNotFoundError as e:
            logger.warning(f'Could not find image file: {e}')

            try:
                # Sleeps two seconds if the OS is late
                sleep(2)

                img_size = os.path.getsize(f"{self.img_path}{id}.jpg")
            except FileNotFoundError as e:
                logger.warning(f'Could not find image attempt two file: {e}')

                img_size = 0
        finally:
            self.total_image_data_size += img_size
            logger.debug(f"total imge data: {self.total_image_data_size}")

    @log_func(logger)
    def is_space_left(self,):
        # 2.9 GB
        max_size = 2.9*10**9
        
        if self.total_image_data_size >= max_size:
            logger.info("Storage not available")
            return False
        else:
            logger.info("Storage available")
            return True
