############------------ IMPORTS ------------############
import bs4 
import requests


############------------ GLOBAL VARIABLE(S) ------------############
words_list = 'http://www-personal.umich.edu/~jlawler/wordlist'

############------------ FUNCTION(S) ------------############
def get_me_that_string():
    '''
     there's only one string in `words_list`
     this function creates a request to the site where 
     that lives, and creates a local copy .txt file
    '''
    request = requests.get(words_list)

    print(request.status_code)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_me_that_string()