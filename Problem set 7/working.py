import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d{0,1}\d)(:(\d\d)){0,1} (A|P)M"
    pt = rf"^{pattern} to {pattern}$"
    match = re.search(pt , s)
    if match:
        num1 = int(match.group(1))
        num3 = int(match.group(5))
        if (0 > num1 or num1 > 12) or (0 > num3 or num3 > 12):
            raise ValueError
        if match.group(2) != None and match.group(2) != ':00':
            num2 = int(match.group(3))
            if 0 > num2 or num2 > 59:
                raise ValueError
            if num2 <= 9:
                num2 = f"0{num2}"
        else:
            num2 = '00'

        if match.group(6) != None and match.group(6) != '00':
            num4 = int(match.group(7))

            if 0 > num4 or num4 > 59:
                raise ValueError

            if num4 <= 9:
                num4 = f"0{num4}"
        else:
            num4 = '00'
        if match.group(4) == 'P' and num1 != 12:
            num1 = num1 + 12
        if match.group(4) == 'A' and match.group(1) == '12':
            num1 = 0
        if match.group(8) == 'P' and num3 != 12:
            num3 = num3 + 12
        if match.group(8) == 'A' and match.group(5) == '12':
            num3 = 0
        if num1 <= 9:
            num1 = f"0{num1}"
        if num3 <= 9:
            num3 = f"0{num3}"

    else:
        raise ValueError
    return f"{num1}:{num2} to {num3}:{num4}"


if __name__ == "__main__":
    main()
