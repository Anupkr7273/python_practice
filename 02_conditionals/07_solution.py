order_size="Medium"
extra_shot= True

if extra_shot:
    coffee=order_size + " Coffee with an exta shot"
else:
    coffee=order_size +"coffee"
    
print("order:",coffee)