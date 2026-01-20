import random

while True:
    n = int(input("Level: "))
    if n > 0:
        num = random.randint(1 , n)
        break
    else:
        continue

while True:
    try:
        guess = int(input("Guess: "))
        if guess == num:
            print("Just right!")
            break

        elif guess > num:
            print("Too large!")

        elif 0 < guess < num:
            print("Too small!")

        else:
            raise ValueError
    except ValueError:
        continue
