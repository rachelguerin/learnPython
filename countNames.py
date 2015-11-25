counts = dict()
names = ['csev','cwen','csev','zqian','cwen','cwen','cwen','cwen','zqian','zqian']
for name in names :
    counts[name] = counts.get(name,0) + 1
    
print counts
