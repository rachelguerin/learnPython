import re  
print sum([int(n) for n in re.findall('[0-9]+',open('regex_sum_186495.txt').read())])