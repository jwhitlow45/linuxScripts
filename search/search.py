import sys
import webbrowser

base_url = "https://duckduckgo.com/?q="
str_to_search = ""

for word in sys.argv[1:]:
    str_to_search = str_to_search + word + '+'

final_url = base_url + str_to_search[:-1]

webbrowser.open(final_url)
print('Opening browser at ' + final_url)
