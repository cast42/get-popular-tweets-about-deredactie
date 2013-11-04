This script depends on following python libraries:
* requests
* BeautifulSoup
* PrettyTable

To install:
* pip install requests
* pip install beautifulsoup4
* pip install PrettyTable

To fetch tweets you must 
go to <http://dev.twitter.com/apps/new> to create an app and get values
for these credentials, which you'll need to provide in place of these
empty string values that are defined as placeholders.
See <https://dev.twitter.com/docs/auth/oauth> for more information
on Twitter's OAuth implementation.

Look in the file redactie.py for the following strings:

    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
    
and fill in your own credentials between the quotes.C
