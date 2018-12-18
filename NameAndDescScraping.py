from bs4 import BeautifulSoup
import requests
import os
import io

'''
this script scraping name and desc text from a digikala.com product which it's link
put in html_link var.
'''

html_link = 'https://www.digikala.com/product/dkp-96891/%D9%87%D8%A7%D8%B1%D8%AF-%D8%A7%DA%A9%D8%B3%D8%AA%D8%B1%D9%86%D8%A7%D9%84-%D8%B3%DB%8C%DA%AF%DB%8C%D8%AA-%D9%85%D8%AF%D9%84-expansion-portable-stea1000400-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-1-%D8%AA%D8%B1%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA'
page_response = requests.get(html_link, timeout = 5)
page_content = BeautifulSoup(page_response.content, "html.parser")

print('----------------- Connected To Server -----------------')

title = page_content.find('h1', attrs={'class' : 'c-product__title'}).text
content = page_content.find('div', {"class" : "c-content-expert__text"}).text

print('----------------- Data Scraped -----------------')

os.chdir('C:\\Users\\Sarkan\\Desktop')
with io.open('data.txt', 'w+', encoding = 'utf-8') as f:
    f.write('Page Title : ' + page_content.title.string + '\ntitleContent : {0}\nDescription : {1}'.format(title, content))
    f.close()

# fi = open('data.txt', 'a')
# fi.write('title : {0}\nDescription : {1}'.format(title, content))
print('----------------- Finished -----------------')
