import twitter
import json
from collections import Counter
from prettytable import PrettyTable
from bs4 import BeautifulSoup
import requests

seen = {}

### https://github.com/edsu/shortpipe/blob/master/shortpipe


def unshorten(url):
    url = url.strip()
    if url in seen:
       return seen[url]

    new_url = url
    try:
        r = requests.get(url)
        if r.status_code == 200:
           new_url = r.url
    except:
        # TODO: maybe log something here?
        pass

    seen[url] = new_url
    return new_url

def get_title(url):
	try:
		r = requests.get(url)
	except:
		print 'Could not get %s' % url
		return 'no title found'
	soup = BeautifulSoup(r.text)
	try:
		title = soup.find("meta", {"name":"title"})['content']
	except:
		print 'no title found for %s' % url
		return "no title found"
	return title
	
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
	
# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

q = 'gva.be'

count = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']


# Iterate through 5 more batches of results by following the cursor

for _ in range(5):
    print "Length of statuses", len(statuses)
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError, e: # No more results when next_results doesn't exist
        break

    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

urls = [ url['expanded_url']
                     for status in statuses
                        for url in status['entities']['urls'] ]
#unshorten_urls = [unshorten_url(url) for url in urls]
unshortend_urls = []
titles = {}

for url in urls:
	if 'gva.be' in url:
		unshortend_url = url
	else:
		print 'Unshorten %s' % url
		unshortend_url = unshorten(url)
	title = get_title(unshortend_url)
	unshortend_urls.append(unshortend_url)
	titles[unshortend_url] = title

c = Counter(unshortend_urls)
pt = PrettyTable(field_names=['Title','Count'])
[ pt.add_row((titles[kv[0]], kv[1])) for kv in c.most_common() ]
pt.align['Title'], pt.align['Count'] = 'l','r'
print pt
