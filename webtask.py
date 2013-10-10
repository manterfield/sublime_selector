import webbrowser
import urllib


GOOGLE = 'google'
STACK = 'stackoverflow'

def google_search(text):
	url = ''.join(('http://www.google.com/#q=', urllib.quote(text), ))
	webbrowser.open(url, new=0, autoraise=True)
	return text


def stackoverflow_search(text):
	url = ''.join((
		'http://www.stackoverflow.com/search?q=',
		urllib.quote(text),
	))
	webbrowser.open(url, new=0, autoraise=True)
	return text