import requests
from bs4 import BeautifulSoup
import os

path = 'C:\\Users\\Sarkan\\Desktop'
work = input('1. Cover\n2. MP3\n3. MP4\nYour Task : ')

link = input('Link : ')
r = requests.get(link)
b = BeautifulSoup(r.content, 'html.parser')

if int(work) == 3:
	s = b.find_all('script')
	script = s[-3]

	songInfo = b.find('div', 'songInfo').find_all('span')
	artist = songInfo[0].string
	title = songInfo[1].string

	while True:
		ch = input('1. 480\n2. 720\n3. 1080\nYour Choice : ')
		try:
			ch = int(ch)
			if ch == 1:
				ch = '480'
				break
			elif ch == 2:
				ch = '720'
				break
			elif ch == 3:
				ch = '1080'
				break
		except ValueError:
			print('the choice is invalid')
		print('Try Again\n')

	string = script.string
	key = "RJ.video{}p = '".format(ch)
	start = string.find(key) + len(key)
	string = string[start:]
	end = string.find('.mp4') + 4
	link = ''

	for i in range(end):
		link += string[i]
		i += 1

	print('Link : ', link)
	hosts = ["https://host1.rjmusicmedia.com","https://host2.rjmusicmedia.com"]

	link0 = "{0}{1}".format(hosts[0], link)
	link1 = "{0}{1}".format(hosts[1], link)

	title = '{0} - {1}.mp4'.format(artist, title)

	rr = requests.get(link0, stream = True)
	with open(title, 'wb') as f:
		print('File Downloading from host 1...')
		for chunk in rr.iter_content(chunk_size = 1024):
			if chunk:
				f.write(chunk)
	f.close()

	filepath = os.path.join(path, title)
	if os.path.getsize(filepath) < 1000000:
		os.remove(filepath)
		print('Host 1 Disconnected')
		rr = requests.get(link1, stream = True)
		with open(title, 'wb') as f:
			print('File Downloading from host 2...')
			for chunk in rr.iter_content(chunk_size = 1024):
				if chunk:
					f.write(chunk)
		f.close()
	print('file downloaded!')
elif int(work) == 1:
	div = b.find('div', 'artwork')
	img = div.find('img')
	title = img.attrs['alt']
	img_url = img.attrs['src']

	#Download image
	r = requests.get(img_url)
	with open('{}.jpg'.format(title), 'wb') as f:
	    f.write(r.content)
	f.close()