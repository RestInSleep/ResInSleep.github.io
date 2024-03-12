# coding: utf-8
import requests
from duckduckgo_search import DDGS

r = requests.get('https://www.bfi.org.uk/lists/10-great-american-film-noirs',  auth = ('user', 'pass'))

from bs4 import BeautifulSoup
import html5lib

soup = BeautifulSoup(r.content, 'html5lib')

soup.find_all('h2')

x = soup.find_all('h2')[0:10]

y = [y.text for y in x]

y = [y.text.strip() for y in x]

y = [y.text.replace(u'\xa0', ' ') for y in x]

paragrafy = soup.find_all('p')
rezyserzy = [p.text.replace(u'\xa0', u' ') for p in paragrafy if p.text.startswith('Director')]
figures = soup.find_all('figure')
figures = figures[1:11]
images = [a.img for a in figures]
images_2 = [a.get('src') for a in images]
images_2
f = open('website.md', 'w')
md = '# American noir pictures\n'
f.write(md)
f.close()
md = ''
l = len(y)
with DDGS() as ddgs:
	for i in range(l):
		f = open(str(i + 1) + '.md', 'w')
		md += ('## ' + str(i + 1) + '. ' + y[i] +  '\n### ' + rezyserzy[i] 
		+ '\n' + '![alt text](' + images_2[i] + ' \"' + y[i] +'\")\n') 
		results = [r for r in ddgs.text( y[i] + ' is a ', timelimit = 'y', max_results = 3)]
		if i == 9:
			md += (results[0]['body'] + '\n')
		else: 
			md += (results[0]['body'] + '\n')
		f.write(md)
		f.close()
		md = ''

