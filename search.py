# https://pypi.org/project/google/

try:
    from googlesearch import search
except ImportError:
    print("No module found.")

# query
q = "Most watched Holdays movies in 2020"

# tld: top level domain
# lan: language
# num: number of results wanted
# start: first result to retrieve
# stop: last result to retrieve
# pause: lapse to wait between HTTP requests
# Return: generator that yields four urls

for i in search(q, tld="com", lang='en', num=10, stop=10, pause=2):
    print(i)