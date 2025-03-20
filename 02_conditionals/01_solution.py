age=input("Enter your age: ")
age_int=int(age)

if age_int < 13:
    print("child")
elif age_int<20:
    print("teenager")
elif age_int<60:
    print("adult")
else:
    print("senior citizen")