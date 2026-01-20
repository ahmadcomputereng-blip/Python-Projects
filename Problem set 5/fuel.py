
def main():
    while True:
        try:
            fuel = (input("Fraction: "))
            frac = convert(fuel)
            break
        except (ValueError , ZeroDivisionError):
            continue
    perc = gauge(frac)
    print(perc)



def convert(fraction):
    x , y = fraction.split("/")
    x = int(x)
    y = int(y)
    if (x > y and y != 0 ) or x < 0 or y < 0 :
        raise ValueError
    frac = x/y * 100
    return(frac)



def gauge(percentage):

    if percentage == 99 or percentage == 100:
        return("F")
    elif percentage == 1 or percentage == 0:
        return("E")
    else:
        return(f"{round(percentage)}%")

if __name__ == "__main__":
    main()
