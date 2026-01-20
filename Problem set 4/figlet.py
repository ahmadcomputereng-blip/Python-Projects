from pyfiglet import Figlet
import sys
try:
    if len(sys.argv) == 1:
        font = 'standard'
    elif len(sys.argv) > 1 and (sys.argv[1]).startswith("-f"):
        font = sys.argv[-1]
    else:
        raise ValueError
    f = Figlet(font)
    user = input("Input: ")
    print("Output:")
    print(f.renderText(user))
except ValueError:
    sys.exit("Invalid usage")
