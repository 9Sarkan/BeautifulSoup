from bs4 import BeautifulSoup
import requests
'''
get link of products which they are in page_link category...

scraping from : digikala.com
'''
page_link = "https://www.digikala.com/search/category-mobile-accessories/"
print('Get all Product link from : {}'.format(page_link))
page_response = requests.get(page_link, timeout = 5)
page_content = BeautifulSoup(page_response.content, "html.parser")

for ul in page_content.find_all('ul', class_= "c-listing__items"):
    for li in ul.find_all('li'):
        a = li.find('a')
        if a != None:
            print(a['href'], a.get_text())
