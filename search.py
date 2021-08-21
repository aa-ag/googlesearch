############------------ IMPORTS ------------############
from selenium import webdriver
import random


############------------ GLOBAL VARIABLE(S) ------------############
url = 'https://www.google.com/'


############------------ FUNCTION(S) ------------############
def search_on():
       '''
        opens list of English words, iterates over
        a random number of them and performs searches
        to confuse data-hungry search engines
       '''
       # open words file, create a list with them, 
       # create a range of N random indexes, slice the list
       # using those indexes to grab and print random words

       words_file = open('words_file', 'r')

       content = words_file.read().splitlines()

       for line in content:
              print(line)

       # creates a webdriver object to open the browser
       # and perform an action in there
       # driver = webdriver.Firefox()

       # get google.com page and perform the search
       # driver.get(url + 'search?q=' + word)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    search_on()