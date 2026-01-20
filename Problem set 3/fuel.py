while True:
    try:
        fuel = (input("Fraction: "))
        x , y = fuel.split("/")
        x = int(x)
        y = int(y)
        if (x > y and y != 0 ) or x < 0 or y < 0 :
            raise ValueError
        fraction = x/y * 100
        if fraction == 99 or fraction == 100:
            print("F")
        elif fraction == 1 or fraction == 0:
            print("E")
        else:
            print(f"{round(fraction)}%")
        break
    except (ValueError , ZeroDivisionError):
        continue
