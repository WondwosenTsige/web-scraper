from bs4 import BeautifulSoup
import requests
import time
sub_string = "citation needed"
url = "https://en.wikipedia.org/wiki/History_of_Mexico"
res = requests.get(url)
list_with_citation = []
soup = BeautifulSoup(res.content, 'html.parser')
pararaph_list = soup.find_all('p')
for item in pararaph_list:
    for string in item.stripped_strings:
        if sub_string in repr(string):
            list_with_citation.append(item.text)
print('Number of citations needed: ', len(list_with_citation))
print()
for paragraph in list_with_citation:
    # print('Original Paragraph \n',paragraph)
    head, sep, tail = paragraph.partition('[')
    print('Stripped Paragraph \n',head)
    print()
    time.sleep(4)