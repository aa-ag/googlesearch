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

    # print(soup.prettify())

    # print(soup.title)

    list_of_unordered_lists = soup.find_all('ul')

    list_of_strings = list()

    for unordered_list in list_of_unordered_lists[5:16]:
        for list_item in unordered_list.text.split('\n'):
            list_item_as_a_string = list_item.replace(u'\xa0', u' ')
            if list_item_as_a_string != '':
                list_of_strings.append(list_item_as_a_string)
            
    print(list_of_strings)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_phrases()