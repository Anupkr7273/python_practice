input_str="teeter"

# for char in input_str:
#     count=0
#     for char_count in input_str:
#         if char==char_count:
#             count+=1
#     if count==1:
#         print("First non repeated character is:",char)
#         break

for char in input_str:
    if input_str.count(char)==1:
        print("char is:",char)
        break