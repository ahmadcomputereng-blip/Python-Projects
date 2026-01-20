import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    rep = len(re.findall(r"\bum\b" , s))
    return rep




if __name__ == "__main__":
    main()
