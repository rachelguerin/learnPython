import re
#read file
fname = raw_input('Enter filename: ')
try:
    fhand = open(fname)
except:
    print 'File could not be opened:',fname
    exit()
    
#get numbers
nums = list()
for line in fhand:
    line = line.rstrip()
    for n in re.findall('[0-9]+',line) :
        nums.append(int(n))
    
#sum
print sum(nums)
