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

    content = request.content

    soup = BeautifulSoup(content, 'html.parser')

    list_of_unordered_lists = soup.find_all('ul')

    txt_file = open('phrases_file', 'w')

    for unordered_list in list_of_unordered_lists[5:16]:
        for list_item in unordered_list.text.split('\n'):
            list_item_as_a_string = list_item.replace(u'\xa0', u' ')
            if list_item_as_a_string != '':
                txt_file.write(list_item_as_a_string + '\n')
            
    print("all set")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_phrases()