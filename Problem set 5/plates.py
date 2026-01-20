def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    if  len(s) > 6 or len(s) < 2 or not (s[:2].isalpha()):
        return False

    for c in range(len(s)):
        if s[c].isdigit() and not(s[c:].isdigit()):
            return False
        if not(s[c].isalpha()) and not(s[c].isdigit()):
            return False
        if s[c] == '0' and s[c-1].isalpha():
            return False
    return True

if __name__ == "__main__":
    main()