import requests
from bs4 import BeautifulSoup
import sys
import os

'''
just add users usernames to download their profile images.
and set the directory you want to save images in it,
'''

lst = []
address = ''

os.chdir(address)
sys.setrecursionlimit(1000000)

def getPhoto(username):
    r = requests.post('https://instadp.net', data = {'username' : username})
    soup = BeautifulSoup(r.content, 'html.parser')
    link = soup.find('img', 'img-responsive').attrs['src']

    with open('{}.jpg'.format(username), 'wb') as f:
        f.write(requests.get(link).content)

    f.close()

for i in lst:
		getPhoto(i)
