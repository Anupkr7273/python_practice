n=int(input("Till what number you want to take sum of even numbers:"))
sum=0
for i in range(0,n+1):
    if i%2==0:
        sum+=i
print("Sum=",sum)