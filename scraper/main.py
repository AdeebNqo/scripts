#
#
# Python script for scraping data from property24.com
#
#
import urllib2
import pickle
from BeautifulSoup import BeautifulSoup

def main():
	#
	# Loading saved html data. The saved data should only be the
	# first page. However, this is written such that you can
	# easily expand.
	#
	saved_data = None
	pageone = None
	try:
		f = open('saved.pkl','r');
		saved_data = pickle.load(f)	
		pageone = saved_data['pageone']
		f.close()
	except IOError:
		print('Error while loading saved data.\nNothing has been nothing, now acting like nothing happened...\n')
	except EOFError:
		print('the cache seems to be empty.')
		#ToDO: delete the cache file
	
	#
	# Loading proper page one
	#
	print('Loading proper page one.')
	if (pageone == None):
		pageone = get_page("http://www.property24.com/for-sale/cape-town/western-cape/432")
	print('parsing page one html...')
	parsed_pageone = BeautifulSoup(pageone)
	#parsing while there's still data pertaining to cape town
	print('supposed to be doing something important here.')
	
	#
	# Now saving pageone for future use -- just in case
	#
	if (pageone!=None):
		print('caching pageone.')
		f = open('saved.pkl','w')
		saved_data={}
		saved_data['pageone'] = pageone
		pickle.dump(saved_data,f)
		f.close()
		#done -- bye bye!
	else:
		print('cannot saved page one. It does not seem to exist.\nHow did that happpen?')

#
# Method for retrieving html, given the website address.
#
def get_page(link):
	return urllib2.urlopen(link).read()

if __name__=="__main__":
	main()
