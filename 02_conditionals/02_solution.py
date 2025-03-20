age=int(input("Give your age:"))
day=str(input("tell me the day of week:"))

# if age<18:
#     pay= 8
# else:
#     pay=12
    
# if day=="wednesday":
#     pay-=2

# print("Pay:")
# print(pay)

price=12 if age>=18 else 8
if day=="wednesday":
    price-=2
print("Ticket price for you is: $",price)