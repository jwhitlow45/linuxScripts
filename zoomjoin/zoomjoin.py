import os
from os.path import expanduser
import sys
import webbrowser
import csv

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
        else:
            raise ValueError('**exception**: invalid command given')        
    except ValueError as error:
        print(error)

# Add meeting to csv
def add():
    # Check argument size
    if ARGSIZE < 3 or ARGSIZE > 4:
        raise ValueError('**exception**: add only takes argument(s) [name link password]')

    # Add name, link, and password (optional) to csv
    with open(CONFIG_FILE, 'a') as config, open(CONFIG_FILE, 'r') as reader:
        # Check for duplicate name
        for row in csv.reader(reader):
            if row[0] == NAME:
                print(f"'{NAME}' already exists...")
                return
        # Write meeting to csv
        writer = csv.writer(config)
        row = [NAME, LINK, PASSWORD]
        writer.writerow(row)
        print(f"'{NAME}' meeting has been created")

# Remove meeting from csv
def remove():
    meeting_removed = False
    # Check argument size
    if ARGSIZE != 2:
        raise ValueError('**exception**: remove only takes argument(s) [name]')

    with open(CONFIG_FILE, 'r') as config, open(TMP_FILE, 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(config):
            if row[0] != NAME:
                writer.writerow(row)
            else:
                meeting_removed = True

    # Delete old config file and replace with new config file
    os.remove(CONFIG_FILE)
    os.rename(TMP_FILE, CONFIG_FILE)
    if meeting_removed:
        print(f"'{NAME}' has been removed")
    else:
        print(f"'{NAME}' does not exist...")

# Completely erase csv file
def clear():
    # Check argument size
    if ARGSIZE != 1:
        raise ValueError('**exception**: clear does not take any arguments')

    response = input('Are you sure you want to remove all meetings?: ').lower()
    if response == 'y' or response == 'yes':
        os.remove(CONFIG_FILE)
        with open(CONFIG_FILE, 'w'):
            pass
        print('Cleared all meetings')
    else:
        print('Aborted removing all meetings...')

# Sort meetings alphabetically
def sort():
    # Check argument size
    if ARGSIZE != 1:
        raise ValueError('**exception**: sort does not take any arguments')

    with open(CONFIG_FILE, 'r') as reader, open(TMP_FILE, 'w') as output:
        rows = []
        for row in csv.reader(reader):
            rows.append(row)
        rows.sort()
        writer = csv.writer(output)
        writer.writerows(rows)

    os.remove(CONFIG_FILE)
    os.rename(TMP_FILE, CONFIG_FILE)
    print('Sorted meetings alphabetically')

# Join meeting in csv
def join():
    # Check argument size
    if ARGSIZE != 2:
        raise ValueError('**exception**: join only takes argument(s) [name]')

    # Join meeting
    with open(CONFIG_FILE, 'r') as config:
        for row in csv.reader(config):
            if row[0] == NAME:
                webbrowser.open(row[1])
                print(f"Joining '{NAME}'...")
                if row[2] != '':
                    print('Password: ' + row[2])
                break

# List all meetings stored in config.csv
def list():
    # Check argument size
    if ARGSIZE != 1:
        raise ValueError('**exception**: list does not take any arguments')

    # List out stored meetings
    with open(CONFIG_FILE, 'r') as config:
        print("Available meetings: ", end='')
        for row in csv.reader(config):
            print(row[0], end=' ')
        print('')

if __name__ == "__main__":
    main()
