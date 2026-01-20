import inflect
p = inflect.engine()
my_list = ["Adieu", "adieu" ]
while True:
    try:
          user = input()
          my_list.append(user)
    except EOFError:
        break

if len(my_list) == 3:
    my_list[2] = "to " + my_list[2]
    print(p.join(my_list, conj ="" ,final_sep=","))
elif len(my_list) == 4:
    my_list[2] = "to " + my_list[2]
    print(p.join(my_list, conj ="and" ,final_sep=""))
elif len(my_list) > 4:
    my_list[2] = "to " + my_list[2]
    print(p.join(my_list))
else:
    print(p.join(my_list, conj = "" , final_sep=","))
