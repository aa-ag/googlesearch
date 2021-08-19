############------------ IMPORTS ------------############
# https://pypi.org/project/google/
import requests
from bs4 import BeautifulSoup
import random


############------------ GLOBAL VARIABLE(S) ------------############
# try:
#     from googlesearch import search
# except ImportError:
#     print("No module found.")

# query
# q = "Most watched Holdays movies in 2020"
# q = "Films de vacances les plus regardés en 2020"

# tld: top level domain
# lan: language
# num: number of results wanted
# start: first result to retrieve
# stop: last result to retrieve -- None would go forever
# pause: lapse to wait between HTTP requests
# Return: generator that yields four urls

# hits = [i for i in search(q, tld="com", lang='fr', num=5, stop=5, pause=2)]
# print(hits)

############------------ FUNCTION(S) ------------############
def search_on():
       text = input("What would you like to search for? ")
       url = 'https://google.com/search?q=' + text
       A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
              )
       
       Agent = A[random.randrange(len(A))]
       
       headers = {'user-agent': Agent}
       r = requests.get(url, headers=headers)
       
       soup = BeautifulSoup(r.text, 'lxml')
       
       for info in soup.find_all('h3'):
              print(info.text)
              print('#######')

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    pass