fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File could not be opened:',fname
    exit()
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()

    for word in words:
        #print word
        if lst == [] : 
            lst.append(word)
        if word not in lst : 
            lst.append(word)
            #print lst   

print sorted(lst)