fname = raw_input('Enter filename: ')
try:
    fhand = open(fname)
except:
    print 'File could not be opened:',fname
    exit()
    
counts=dict()

for line in fhand:
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0)+1


lst = sorted( [ (v,k) for k,v in counts.items()])

for v,k in lst[len(lst)-10:] :
    print k,v