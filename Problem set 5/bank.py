def main():
    greet = input("Greeting: ")
    pay = value(greet)
    print(f"${pay}")

def value(greeting):
    greeting = greeting.lower().strip()
    if (greeting.startswith("hello") or greeting.startswith("Hello")):
        return (0)
    elif (greeting.startswith("h") or greeting.startswith("H")):
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()
