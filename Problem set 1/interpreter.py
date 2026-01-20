#implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z
e = input("Expression: ")
x, y, z = e.split()
x = int(x)
z = int(z)
if (y == '+'):
    res = float (x + z)
    print(f"{res:.1f}")
elif (y == '-'):
    res = float (x - z)
    print(f"{res:.1f}")
elif (y == '/'):
    res = float (x / z)
    print(f"{res:.1f}")
elif (y == '*'):
    res = float (x * z)
    print(f"{res:.1f}")
