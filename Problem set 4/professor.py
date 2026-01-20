import random

def main():
    score = 0
    lvl = get_level()
    for i in range(10):
        t = 0
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        while True:
            try:
                n = int(input(f"{x} + {y} = "))
                if n == (x+y):
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                t = t + 1
            if t == 3:
                print(f"{x} + {y} = {x+y}")
                break
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
            else:
                raise ValueError
        except ValueError:
            continue

def generate_integer(level):

    if level == 1:
        num = random.randint(0 , 9)
    elif level == 2:
        num = random.randint(10 , 99)
    elif level == 3:
        num = random.randint(100 , 999)

    return num

if __name__ == "__main__":
    main()
