import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
count = raw_input('Enter count:')
position = raw_input('Enter position:')

allnames = list()
c=0
while c < int(count) :
    
    print 'Retrieving:'+url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    names = soup('a')
    namecount = 0

    for name in names:
        namecount = namecount+1
        if namecount==int(position):
            nextURL = name.get('href',None)
            break

    allnames.append(nextURL)
    
    url = nextURL
    c = c+1

print 'Last Url:',url