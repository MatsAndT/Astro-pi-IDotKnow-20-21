#!/usr/bin/env python3
import getopt
import logging
import sys

from util.logging import stream_handler


class AstroPi:
    HELP = '''
    Usage main.py [OPTIONS]...

    Options:
        -h  --help          Prints usage and help
        -v  --verbose       Print debug info
    '''

    def __init__(self):
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

        self._logger = logging.getLogger(__name__)
        self._logger.addHandler(stream_handler)

        self._logger.setLevel(logging.DEBUG)
        stream_handler.setLevel(logging.INFO)

        for option, arg in options:
            if option in ('-v', '--verbose'):
                self._logger.setLevel(logging.DEBUG)
                stream_handler.setLevel(logging.DEBUG)
            elif option in ('-h', '--help'):
                print(self.HELP)

    def main(self):
        while True:
            pass  # Main loop here


if __name__ == '__main__':
    astro = AstroPi()
    astro.main()
