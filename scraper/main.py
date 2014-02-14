#
#
# Python script for scraping data from property24.com
#
#
import urllib2
def main():
	print('\t-Property24 address and price scraper--')
	page = get_page("http://www.property24.com/for-sale/cape-town/western-cape/432")
	print(page)
def get_page(link):
	return urllib2.urlopen(link).read()
if __name__=="__main__":
	main()
