#!/usr/bin/env python3
import getopt
import logging
import sys
import os

from util.log import get_logger, set_level
from util.camera import AstroCamera
from util.space import is_space_left


class AstroPi:
    HELP = '''
    Usage main.py [OPTIONS]...

    Options:
        -h  --help          Prints usage and help
        -v  --verbose       Print debug info
    '''

    output_path = 'output/'

    camera = AstroCamera.with_settings_preset()

    def __init__(self):

        try:
            os.mkdir(os.path.join(self.output_path, 'images'))
        except FileExistsError:
            pass

        try:
            options, args = getopt.getopt(
                sys.argv[1:],
                'vh',
                ('verbose', 'help')
            )
        except getopt.GetoptError as e:
            print(e.msg)
            print(self.HELP)
            sys.exit(2)

        for option, arg in options:
            if option in ('-v', '--verbose'):
                set_level(logging.DEBUG)
            elif option in ('-h', '--help'):
                print(self.HELP)

        self._logger = get_logger('astro')
        self._logger.debug('Program started')

    def main(self):
        while True:
            if not is_space_left(self.output_path):
                self._logger.info(f'Storage space limit reached! Exiting...')
                break
            img = self.camera.capture_astroimage()
            img.save(os.path.join('output', 'images', f'{img.id}.jpg'))
            self._logger.debug(f'Image <id: {img.id}> captured.')


if __name__ == '__main__':
    astro = AstroPi()
    astro.main()
