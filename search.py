############------------ IMPORTS ------------############
from selenium import webdriver
import random
import time


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

       words_list = list(word for word in content if word != '')

       # print(len(words_list))
       # 69903

       ten_indexes = generate_ten_random_numbers()

       ten_random_words = list(words_list[indx] for indx in ten_indexes)

       # print(ten_random_words)

       # creates a webdriver object to open the browser
       # and perform an action in there
       driver = webdriver.Firefox()

       for _ in ten_random_words:

              # get google.com page and perform the search
              driver.get(url + 'search?q=' + _)
              time.sleep(5)

       ## TO DO: make number of seconds random too
       ## TO DO: divide search_on() into 
       # words and search functions
       ## TO DO: add phrases to the bank/list of possible searches
       # https://www.englishspeak.com/en/english-phrases?category_key=3


def generate_up_to_ten_random_numbers():
       '''
        helper function to generate a random upper limit
        to a random list of numbers
        to use as indexes to slice wors in `search_on()`
       '''
       upper_limit = random.randint(1, 10)

       return random.sample(range(0, 69903), upper_limit)


def generate_random_number_of_seconds():
       return random.randint(1, 180)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # search_on()
    
    # print(generate_up_to_ten_random_numbers())
    print(generate_random_number_of_seconds())