from bs4 import *
import urllib2,time,os
while True:
	print "Reading Score....."
	url = "http://vcricket.com"
	link = urllib2.urlopen(url).read()
	os.system('cls')       # Linux use 'clear'
	soup = BeautifulSoup(link,"html.parser")
	s=soup.find('span',{ "class" : 'brclr'} )
	print "Current Score Is",s.text
	print s.text
	time.sleep(10)
	os.system('cls')    # Linux  use 'clear'  
	
	
