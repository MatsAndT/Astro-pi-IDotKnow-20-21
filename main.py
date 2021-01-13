#!/usr/bin/env python3
import getopt
import logging
import sys

from util.logging import get_logger, set_level


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

        for option, arg in options:
            if option in ('-v', '--verbose'):
                set_level(logging.DEBUG)
            elif option in ('-h', '--help'):
                print(self.HELP)

        self._logger = get_logger(__name__)

    def main(self):
        while True:
            pass  # Main loop here


if __name__ == '__main__':
    astro = AstroPi()
    astro.main()
