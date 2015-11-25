addr = raw_input('Enter URL: ')

import urllib
fhand = urllib.urlopen(addr)

for line in fhand:
    print line.strip()
    