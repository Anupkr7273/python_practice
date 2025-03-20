year=int(input("Enter the year: "))
if year%4==0:
    leap=True
    if year%100==0 and year%400!=0:
        leap=False
else:
    leap= False

print("Leap year: ",leap)    
