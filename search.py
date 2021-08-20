############------------ IMPORTS ------------############
from selenium import webdriver


############------------ GLOBAL VARIABLE(S) ------------############
url = 'https://www.google.com/'


############------------ FUNCTION(S) ------------############
def search_on():
       '''
        opens list of English words, iterates over
        a random number of them and performs searches
        to confuse data-hungry search engines
       '''
       # hardcoding a word to search on googl
       test_word = 'hello'

       # creates a webdriver object to open the browser
       # and perform an action in there
       driver = webdriver.Firefox()

       # get google.com page and perform the search
       driver.get(url + 'search?q=' + test_word)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    search_on()