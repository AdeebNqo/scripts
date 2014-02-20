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
		print('Error while loading saved data.\nNothing has been done, now acting like nothing happened...\n')
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
	pageone_soup = BeautifulSoup(pageone)
	#parsing while there's still data pertaining to cape town
	
	##Finding the number of available residences
	toolbox = pageone_soup.find('div', {'class':'p24_toolBox'})
	lists = toolbox.findAll('li')
	for item in lists:
		if (item != None):
				spans = item.findAll('span')
				if (len(spans)==1):
					num = spans[0]
					split_nums = num.text.split()
					last_index = len(split_nums)-1
					num_per_page =split_nums[last_index-2]
					num = split_nums[last_index]
					print('there are '+num+' items, '+num_per_page+' per page')
	#Finding the list of houses in a page
	column = pageone_soup.findAll('div',{'class':'col-xs-8'})
	column.pop()
	column.pop()
	houses_container = column.pop()
	houses = houses_container.findAll('div',{'class':'p24_panel p24_panelHighlight p24_listingTile js_P24_listingTileContainer'})
	for house in houses:
		house_info = get_house_info(house)
		print(house_info)

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
#
# Method for getting simple info on a house using
# a p24 ad box thingie
#
def get_house_info(housedata):
	print('getting res')
	return 'house'
	
if __name__=="__main__":
	main()
