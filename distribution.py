fname = raw_input('Enter filename: ')
try:
    fhand = open(fname)
except:
    print 'File could not be opened:',fname
    exit()
count=dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):continue
    
    words = line.split()
    #print words[5]
    t = words[5].split(':')
    #print t
    hr = t[0]
    #print hr
    count[hr] = count.get(hr,0)+1

tmp = list()
for k,v in count.items():
    tmp.append( (k,v) )

tmp.sort()

for k,v in tmp :
    print k,v

 