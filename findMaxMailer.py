fname = raw_input('Enter filename: ')
try:
    fhand = open(fname)
except:
    print 'File could not be opened:',fname
    exit()
    
counts=dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):continue
    words = line.split()
    counts[words[1]] = counts.get(words[1],0)+1
 
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count 
print bigword,bigcount