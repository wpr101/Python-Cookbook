import urllib
import mechanize
from bs4 import BeautifulSoup
from urlparse import urlparse

def getPic (search):
	try:
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		browser.addheaders = [('User-agent', 'Mozilla')]

		htmltext = browser.open("https://www.google.ee/search?q=orange+apple&biw=1347&bih=677&source=lnms&tbm=isch&sa=X")
		img_urls = []
		soup = BeautifulSoup(htmltext, "lxml")
		print(soup)
		results = soup.findAll("a")
		#print (results)


		


	except:
		print ("error")

getPic("Orange Apple")
