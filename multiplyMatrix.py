M1 = [[2,3],[4,5],[6,7]]
M2 = [[2,3,4],[4,5,6]]
A = []

for i in range(0,len(M1)):
    print 'i:',i
    print 'M1[i]',M1[i]
    for j in range(0,len(M1[i])):
        print 'j:',j
        print 'M1[i][j]:',M1[i][j]
