import httplib
import urllib2
import requests
import time

def One():

    c = httplib.HTTPConnection('www.nameamigo2.com')
    try:
    	c.request("HEAD", '')
    	if c.getresponse().status < 400:
            print('web site exists')
    except:
        print('web site does not exist')

def Two():
   
    try:
    	code = urllib2.urlopen('http://www.nameamigo2.com')
	if code < 400:
	    print('web site exists')
    except:
        print('web site does not exist')

#slowest
def Three():

    try:
    	request = requests.get('http://www.nameamigo2.com')
    	if request.status_code < 400:
            print('web site exists')
    except:
        print('web site does not exist')

t0 = time.time()
One()
t1 = time.time()
total = t1-t0
print("One", total)

t0 = time.time()
Two()
t1 = time.time()
total = t1-t0
print("Two", total)

t0 = time.time()
Three()
t1 = time.time()
total = t1-t0
print("Three", total)

