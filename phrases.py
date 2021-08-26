############------------ DOCUMENTATION ------------############
# https://beautiful-soup-4.readthedocs.io/en/latest/


############------------ IMPORTS ------------############
from bs4 import BeautifulSoup
import requests


############------------ GLOBAL VARIABLE(S) ------------############
url = 'https://grammarvocab.com/1000-most-common-english-phrases-with-pdf/'


############------------ FUNCTION(S) ------------############
def get_phrases():
    '''
     request url, bs4 elements,
     create a local copy with all 
     for later use
    '''
    request = requests.get(url)

    if request.status_code != 200:
        return "Something's not right"

    page = request.content

    soup = BeautifulSoup(page, 'html.parser')

    print(soup.prettify())


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_phrases()