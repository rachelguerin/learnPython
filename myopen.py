fname = raw_input('Enter filename: ')
try:
    fhand = open(fname)
except:
    print 'File could not be opened:',fname
    exit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print 'There were ', count, ' subject lines in ',fname