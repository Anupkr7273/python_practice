marks=int(input("Enter your marks:"))
if marks>=101:
    print("please verify your marks")
    exit()
if marks<60:
    grade="F"    
elif marks<70:
    grade="D"  
elif marks<80:
    grade="C"
elif marks<90:
    grade="B"
else:
    grade="A" 
print (grade)