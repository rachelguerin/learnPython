import json
import urllib

url = raw_input('Enter location:')

print 'Retrieving',url
input = urllib.urlopen(url).read()
print 'Retrieved',len(input),'characters'
info = json.loads(input)

comments = info["comments"]

sum = 0
count = 0
for comment in comments:
    sum = sum + int(comment["count"])
    count = count + 1

print 'Count:', count
print 'Sum:', sum

