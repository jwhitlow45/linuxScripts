import webbrowser
import csv

from zoomjoin import *

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

    # Store all rows of csv in a list to be sorted
    with open(CONFIG_FILE, 'r') as reader, open(TMP_FILE, 'w') as output:
        rows = []
        for row in csv.reader(reader):
            rows.append(row)
        # Prevent unnecessary sorting
        if len(rows) < 2:
            os.remove(TMP_FILE)
            raise ValueError('**exception**: too few meetings to sort')

        rows.sort()
        writer = csv.writer(output)
        writer.writerows(rows)

    # Overwrite old config with new config file
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

# List all commands
def help():
    # Check argument size
    if ARGSIZE != 1:
        raise ValueError('**exception**: help does not take any arguments')

    print('Available commands are:')
    print('zm add [name] [link] [password]  # Add meeting to list')
    print('zm remove [name]                 # Remove meeting from list')
    print('zm join [name]                   # Join meeting')
    print('zm list                          # Show list of meetings')
    print('zm sort                          # Sort meetings in list alphabetically')
    print('zm clear                         # Remove all meetings from list')
