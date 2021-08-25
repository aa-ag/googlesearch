############------------ IMPORTS ------------############
from selenium import webdriver
import random
import time


############------------ GLOBAL VARIABLE(S) ------------############
# url = 'https://www.google.com/'
url = 'https://www.youtube.com/'


############------------ FUNCTION(S) ------------############
###--- HELPER FUNCTION(S) ---###
def generate_up_to_ten_random_numbers():
       '''
        helper function to generate a random upper limit
        to a random list of numbers
        to use as indexes to slice wors in `search_on()`
       '''
       upper_limit = random.randint(1, 10)

       return random.sample(range(0, 69903), upper_limit)


def generate_random_number_of_seconds():
       '''
        generates a random int from 1 to 30
       '''
       return random.randint(1, 30)


def get_the_words_and_make_a_list():
       # open words file, create a list with them, 
       # create a range of N random indexes, slice the list
       # using those indexes to grab and print random words

       words_file = open('words_file', 'r')

       content = words_file.read().splitlines()

       words_list = list(word for word in content if word != '')

       # print(len(words_list))
       # 69903

       return words_list


###--- SEARCH FUNCTION(S) ---###
def search_on():
       '''
        opens list of English words, iterates over
        a random number of them and performs searches
        to confuse data-hungry search engines
       '''
       words = get_the_words_and_make_a_list()

       random_indexes = generate_up_to_ten_random_numbers()

       random_words = list(words[indx] for indx in random_indexes)

       # creates a webdriver object to open the browser
       # and perform an action in there
       driver = webdriver.Firefox()

       for word in random_words:
              # generate a random number of seconds up to 180
              random_number_of_seconds = generate_random_number_of_seconds()

              # print(word)
              # get google.com page and perform the search
              # driver.get(url + 'search?q=' + word)

              # get youtube.com page and perform the search
              driver.get(url + 'results?search_query=' + word)

              # give the page 3 seconds to load
              time.sleep(random_number_of_seconds + 0.33)

              # scroll down
              driver.execute_script("window.scrollTo(0, 3000);")

              # give the page 3 seconds to load
              time.sleep(random_number_of_seconds - 0.33)

              # scroll further down
              driver.execute_script("window.scrollTo(0, 6000);")

              time.sleep(random_number_of_seconds + 0.66)

              # scroll up
              driver.execute_script("window.scrollTo(0, 0);")

              # take a little breather to seem human
              time.sleep(random_number_of_seconds)

       ## TO DO: add phrases to the bank/list of possible searches
       ## cool to do: Type one letter at the time
       ## cool to do: Translate into other languages via API

       driver.close()
       
       print("All done for now 😉")



############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    search_on()