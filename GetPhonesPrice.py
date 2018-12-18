from bs4 import BeautifulSoup
import requests
import os
import io

'''
get Huawei or samsung phones price form mobile.ir and save it in a txt file on desktop
'''
huawei = 'https://www.mobile.ir/brands/111-huawei.aspx?sort=date&dir=desc&withprice=true&product_class=All'
samsung = 'https://www.mobile.ir/brands/2-samsung.aspx?sort=date&dir=desc&withprice=true&product_class=All'

while True:
	try:
		i = input('Please Choice a brand : \n1. Samsung\n2. Huawei\nYour Choice : ')
		if i == '1':
			page_url = samsung
			break
		elif i == '2':
			page_url = huawei
			break
		else:
			print('Please Choice a valid choice.')
	except:
		print('Try Again.')

page_response = requests.get(page_url, timeout = 5)
page_content = BeautifulSoup(page_response.content, 'html.parser')

divAv = page_content.find_all('div',"phone Available")

phones = ['Name     Price',]

for i in divAv:
    a = i.find('div', 'info')
    name = a.find('h4')
    name = name.find('a').string
    price = a.find('h6').string
    phones.append('{0},     {1}'.format(name, price))

print('----------- info scraping ------------')

#The place you want to save file on it
os.chdir('C:\\Users\\Sarkan\\Desktop\\')
with io.open('Price.txt', 'w+', encoding='utf-8') as f:
    f.write('\n'.join(phones))
    f.close()

print('----------- file saved ------------')