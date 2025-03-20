input_string=str(input("Give the string you want the reverse of:"))
rev_str=""
# print(type(input_string))
for char in input_string:
    rev_str=char + rev_str
print("Reverse string:",rev_str)