my_dict = {}
while True:
    try:
        fruit = input().strip().upper()
        if fruit in my_dict:
            my_dict[fruit] = my_dict[fruit]+1
        else:
            my_dict[fruit] = 1
    except EOFError:
        break
sorted_dict = dict(sorted(my_dict.items()))
for k , v in sorted_dict.items():
    print (f"{v} {k}")
