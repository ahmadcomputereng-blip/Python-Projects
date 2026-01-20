import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    byte = r"((1{0,1}[0-9]{1,2})|(25[0-5])|(2[0-4][0-9]))"
    pattern = rf"^{byte}\.{byte}\.{byte}\.{byte}$"
    match = re.search(pattern, ip)
    if match:
        return True
    return(False)



if __name__ == "__main__":
    main()
