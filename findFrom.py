fname = raw_input('Enter filename: ')
try:
    fhand = open(fname)
except:
    print 'File could not be opened:',fname
    exit()
count=0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):continue
    count = count+1
    words = line.split()
    #domain = words[1].split('@')
    #print domain[1]
    print words[1]
        
print "There were", count, "lines in the file with From as the first word"