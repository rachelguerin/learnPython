import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

spans = soup('span')

nums = list()
for span in spans:
    nums.append(int(span.contents[0]))
print sum(nums)
