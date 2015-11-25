def computepay(h,r):
    if h <= 40:
        pay = r * h
    else :
        pay = r * 40 + (r * 1.5 * (h - 40))
    return pay


try:
    inp = raw_input("Enter hours: ")
    hours = float(inp)
    inp = raw_input("Enter rate: ")
    rate = float(inp)
except:
    print "Error, please enter numeric input."
    quit()
    
print computepay(hours, rate)