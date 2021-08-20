############------------ IMPORTS ------------############
import bs4 
import requests


############------------ GLOBAL VARIABLE(S) ------------############
words_list = 'http://wsonal.umich.edu/~jlawler/wordlist'

############------------ FUNCTION(S) ------------############
def get_me_that_string():
    '''
     there's only one string in `words_list`
     this function creates a request to the site where 
     that lives, and creates a local copy .txt file
    '''
    try:
        request = requests.get(words_list)

        if request.status_code != 200:
            print("Whoops! Something went wrong...")
            exit()

        print(request.content)
    except:
        print("Whoops! Something went wrong...")



############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_me_that_string()