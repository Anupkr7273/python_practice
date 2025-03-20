distance=int(input("Enter the distance: "))

if distance <3:
    transport="walk"
elif distance <=15:
    transport="Bike"
else:
    transport="Car"
    
print(transport)