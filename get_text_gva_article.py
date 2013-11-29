from bs4 import BeautifulSoup
import requests

urls = ['http://www.gva.be/nieuws/multimedia/aid1496967/exclusief-interview-met-de-stem-achter-super-mario.aspx',
'http://m.gva.be/nieuws/binnenland/aid988952/pasen-hemelvaartsdag-en-allerheiligen-geen-wettelijke-feestdagen-meer.aspx']


def get_title_and_text(url):
	try:
		r = requests.get(url)
	except:
		print 'Could not get %s' % url
		return ('no title found',"")
	soup = BeautifulSoup(r.text)
	if url.startswith('http://www.gva.be/'):
		try:
			title = soup.find("meta", {"name":"title"})['content']
			art_text = ''
			for sibling in soup.find('span',attrs={"class":"date-marker"}).find_next_siblings():
				art_text += sibling.text
		except:
			print 'no title or article text found for %s' % url
			return ("no title found","")
	elif url.startswith('http://m.gva.be/'):
		try:
			title = soup.find("meta", {"property":"og:title"})['content']
			art_text = soup.find('div', attrs={'class':'txt'}).text
		except:
			print 'no title or article text found for %s' % url
			return ("no title found","")
	else:
		print 'no title or article text found for %s' % url
		return ("no title found","")

	return (title, art_text)

for url in urls:
	title, text = get_title_and_text(url)
	print text
