# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File could not be opened:',fname
    exit()
count = 0
sum = 0    
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    length = len(line)
    count = count + 1
    sum = sum + float(line[length-7:])

avg = sum / count
print 'Average spam confidence:',avg