############------------ IMPORTS ------------############
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

    if request.status_code != 200:
        print("Whoops! Something went wrong...")
        exit()

    big_string = request.content.decode("utf-8")

    words_tx_file = open('words_txt_file', 'w')
        
    for word in big_string.split('\r'):
        words_tx_file.write(word)

    print("all set.")



############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_me_that_string()