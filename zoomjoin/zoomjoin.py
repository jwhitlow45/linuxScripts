import sys
import webbrowser

from config import links, passwords

def main(arg):
    try:
        webbrowser.open(links[arg])
        if arg in passwords.keys():
            print("Password: " + passwords[arg])
    except KeyError:
        print("*exception*: Not a valid argument! Valid arguments are:")
        print(*list(links.keys()))

if __name__ == "__main__":
    try:
        argSize = len(sys.argv)
        if (argSize < 2) or (argSize > 2):
            raise ValueError
        else:
            main(sys.argv[1])
    except ValueError:
        print("*exception*: Script can only have one arugment!")
