import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
count = raw_input('Enter count:')
position = raw_input('Enter position:')

urlFirst = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_'


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
            nextname = name.contents[0]
            break

    allnames.append(nextname)
    
    url = urlFirst+nextname+'.html'
    c = c+1

print 'Last Url:',url