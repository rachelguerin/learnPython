fname = raw_input('Enter filename: ')
try:
    fh = open(fname)
except:
    print 'File could not be opened:',fname
    exit()

for line in fh:
    line = line.rstrip()
    print line.upper()