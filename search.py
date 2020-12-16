# https://pypi.org/project/google/

try:
    from googlesearch import search
except ImportError:
    print("No module found.")

# query
# q = "Most watched Holdays movies in 2020"
q = "Films de vacances les plus regardés en 2020"

# tld: top level domain
# lan: language
# num: number of results wanted
# start: first result to retrieve
# stop: last result to retrieve -- None would go forever
# pause: lapse to wait between HTTP requests
# Return: generator that yields four urls

hits = [i for i in search(q, tld="com", lang='fr', num=100, stop=100, pause=2)]

print(hits)