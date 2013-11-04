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

prefixes = ['http://www.deredactie.be/cm/vrtnieuws/',
	        'http://deredactie.be/cm/vrtnieuws/',
	        'http://www.deredactie.be/cm/',
	        'http://www.deredactie.be/permalink/',
	        'http://m.deredactie.be/cm/vrtnieuws.mobile/',
	        'http://www.deredactie.be/cm/vrtnieuws.english/',
	        'http://www.deredactie.be/cm/vrtnieuws.francais/',
	        'http://www.deredactie.be/cm/vrtnieuws.deutsch']

def clean(url):
	for prefix in prefixes:
		if url.startswith(prefix):
			url = url[len(prefix):] # remove prefix
			url, questionmark, tail = url.partition('?') #remove everything after ?
			return url
	return 'no prefix found'

def is_deredactie_url(url):
	for prefix in prefixes:
		if url.startswith(prefix):
			return True
	return False

def get_permalink_and_title(url):
	try:
		r = requests.get(url)
	except:
		print 'Could not get %s' % url
		return 'no permalink found'
	soup = BeautifulSoup(r.text)
	if 'm.deredactie' in url:
		try:
			permalink = soup.find("link", {"rel":"canonical"})['href']
			for tag in soup.find_all('title'):
				title = tag.text
				break
		except:
			print 'no permalink found for %s' % url
			return ('no permalink found',"no title found")
	else:
		try:
			permalink = soup.find("meta", {"property":"og:url"})['content']
			title = soup.find("meta", {"property":"og:title"})['content']
		except:
			print 'no permalink found for %s' % url
			return ('no permalink found',"no title found")
	return (permalink, title)

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

q = 'deredactie'

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
	if 'deredactie.be' in url:
		unshortend_url = url
	else:
		#print 'Unshorten %s' % url
		unshortend_url = unshorten(url)
	if is_deredactie_url(unshortend_url):
		permalink,title = get_permalink_and_title(unshortend_url)
		#clean_url = clean(unshortend_url)
		unshortend_urls.append(permalink)
		titles[permalink] = title
	else:
		print "Geen deredactie url: %s" % unshortend_url

c = Counter(unshortend_urls)
pt = PrettyTable(field_names=['Title','Count'])
[ pt.add_row((titles[kv[0]], kv[1])) for kv in c.most_common() ]
pt.align['Title'], pt.align['Count'] = 'l','r'
print pt
