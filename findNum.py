text = "X-DSPAM-Confidence:    0.8475";
nStart = text.find('0')
nEnd = len(text)
num = text[nStart:nEnd+1]
print float(num)