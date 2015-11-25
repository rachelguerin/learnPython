try:
    inp = raw_input("Enter score: ")
    score = float(inp)
except:
    print "Error, please enter numeric input."
    quit()

if score > 1 : 
    grade = "Invalid score. Please enter a value between 0 and 1." 
elif score >= 0.9 :
    grade = "A"
elif score >= 0.8 :
    grade = "B" 
elif score >= 0.7 :
    grade = "C"
elif score >= 0.6 :
    grade = "D"
elif score < 0.6 :
    grade = "F"    
else :
    grade = "Invalid score. Please enter a value between 0 and 1."

print grade