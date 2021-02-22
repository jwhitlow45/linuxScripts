import os
from os.path import expanduser
import sys

from commands import *

# GLOBAL VARIABLES
ARGSIZE = len(sys.argv) - 1

# ARGUMENTS
COMMAND = sys.argv[1]
NAME = ''
LINK = ''
PASSWORD = ''
if ARGSIZE > 1:
    NAME = sys.argv[2]
if ARGSIZE > 2:
    LINK = sys.argv[3]
if ARGSIZE > 3:
    PASSWORD = sys.argv[4]

# PATHS
HOME = expanduser('~')
CONFIG_FILE = HOME + '/scripts/zoomjoin/config.csv'
TMP_FILE = HOME + '/scripts/zoomjoin/tmp.csv'

def main():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w'):
            print('Created initial config file...')

    try:
        if COMMAND == 'add':
            add()
        elif COMMAND == 'remove':
            remove()
        elif COMMAND == 'clear':
            clear()
        elif COMMAND == 'sort':
            sort()
        elif COMMAND == 'join':
            join()
        elif COMMAND == 'list':
            list()
        elif COMMAND == 'help':
            help()
        else:
            raise ValueError('**exception**: invalid command given')        
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()
