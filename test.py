for x in range(1,100):
    result = ""
    if x%3 == 0:
        result = "fizz"
    if x%5 == 0:
        result = result + "buzz"
    if x%7 == 0:
        result = result + "BRUM"    
    if result == "":
        result = x

    print result