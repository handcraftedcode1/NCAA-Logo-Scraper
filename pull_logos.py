from bs4 import BeautifulSoup
import urllib
import pprint
import string
import tempfile

urls = [
		'http://www.sportslogos.net/teams/list_by_league/30/NCAA_Division_I_a-c/NCAA_a-c/logos/',
		'http://www.sportslogos.net/teams/list_by_league/31/NCAA_Division_I_d-h/NCAA_d-h/logos/',
		'http://www.sportslogos.net/teams/list_by_league/32/NCAA_Division_I_i-m/NCAA_i-m/logos/',
		'http://www.sportslogos.net/teams/list_by_league/33/NCAA_Division_I_n-r/NCAA_n-r/logos/',
		'http://www.sportslogos.net/teams/list_by_league/34/NCAA_Division_I_s-t/NCAA_s-t/logos/',
		'http://www.sportslogos.net/teams/list_by_league/35/NCAA_Division_I_u-z/NCAA_u-z/logos/'
]

for url in urls:

	print 'Loading HTML...'
	s = urllib.urlopen(url)
	html = s.read()

	soup = BeautifulSoup(html)
	for li in soup.find_all('img'):
		filename = unicode(li.string).strip().replace(' ','') + '.gif'
		image_url = li['src']

		print tempfile.gettempdir() # prints the current temporary directory
		print 'Downloading ' + filename + '...'
		urllib.urlretrieve(image_url, filename)