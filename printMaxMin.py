largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done":
        break
    try:
        num = float(inp)
        if largest is None:
            largest = num
            smallest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
        	largest = num
    except:
        print "Invalid input"
        continue
    #print int(num)
print "Maximum is",int(largest)
print "Minimum is",int(smallest)