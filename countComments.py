import urllib
import xml.etree.ElementTree as ET


url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum = 0
c = 0
for count in counts:
    sum = sum + int(count.text)
    c = c+1

print 'Count:',c
print 'Sum:',sum

