import logging
import os
from time import sleep

logger = logging.getLogger('astro')

class Space:
    total_image_data_size = 0

    def add_size(self, id):
        try:
            img_size = os.path.getsize("{}{}.jpg".format(self.img_path, id))
            logger.debug("img_size: {}".format(img_size))
        except FileNotFoundError as e:
            logger.warning('Could not find image file: {}'.format(e))

            try:
                # Sleeps two seconds if the OS is late
                sleep(2)

                img_size = os.path.getsize("{}{}.jpg".format(self.img_path, id))
            except FileNotFoundError as e:
                logger.warning('Could not find image attempt two file: {}'.format(e))

                img_size = 0
        finally:
            self.total_image_data_size += img_size
            logger.debug("total imge data: {}".format(self.total_image_data_size))

    def is_space_left(self,):
        logger.debug('Function storage_available start')
        
        # 2.9 GB
        max_size = 2.9*10**9
        
        if self.total_image_data_size >= max_size:
            logger.info("Storage not available")
            return False
        else:
            logger.info("Storage available")
            return True

        logger.debug('Function storage_available end')