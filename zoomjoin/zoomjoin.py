import os
import sys
import webbrowser
import csv

# GLOBAL VARIABLES
ARGSIZE = len(sys.argv) - 1

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

HOME = os.path.expanduser('~')
CONFIG_FILE = HOME + '/scripts/zoomjoin/config.csv'
TMP_FILE = HOME + '/scripts/zoomjoin/tmp.csv'

def main():
    try:
        if COMMAND == 'add':
            add()
        elif COMMAND == 'remove':
            remove()
        elif COMMAND == 'join':
            join()
        elif COMMAND == 'list':
            list()
        else:
            raise ValueError('**exception**: invalid command given')        
    except ValueError as error:
        print(error)

# Add meeting to csv
def add():
    # Check argument number
    if ARGSIZE < 3 or ARGSIZE > 4:
        raise ValueError('**exception**: add only takes argument(s) [name link password]')

    # Add name, link, and password (optional) to csv
    with open(CONFIG_FILE, 'w') as config:
        writer = csv.writer(config)
        row = [NAME, LINK, PASSWORD]
        writer.writerow(row)

# Remove meeting from csv
def remove():
    # Check argument number
    if ARGSIZE != 2:
        raise ValueError('**exception**: remove only takes argument(s) [name]')

    with open(CONFIG_FILE, 'r') as config, open(TMP_FILE, 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(config):
            if row[0] != NAME:
                writer.writerow(out)

    os.remove(CONFIG_FILE)
    os.rename(TMP_FILE, CONFIG_FILE)

# Join meeting in csv
def join():
    # Check argument number
    if ARGSIZE != 2:
        raise ValueError('**exception**: join only takes argument(s) [name]')

    # Join meeting
    with open(CONFIG_FILE, 'r') as config:
        for row in csv.reader(config):
            if row[0] == NAME:
                webbrowser.open(row[1])
                if row[2] != '':
                    print('Password: ' + row[2])

# List all meetings stored in config.csv
def list():
    # Check argument number
    if ARGSIZE != 1:
        raise ValueError('**exception**: list does not take any arguments')

    # List out stored meetings
    with open(CONFIG_FILE, 'r') as config:
        print("Stored meetings: ", end='')
        for row in csv.reader(config):
            print(row[0], end=' ')
        print('')

if __name__ == "__main__":
    main()
