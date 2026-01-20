import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith(".py")):
    sys.exit("Not a Python file")
try:
    with open(sys.argv[1] , "r") as f:
        count = 0
        for line in f:
            line = line.lstrip()
            if not (line.startswith('#')) and (line != ''):
                count = count + 1
            
except FileNotFoundError:
    sys.exit("File does not exist")
print(count)
# l = []
# for line in content :
#     if (line.lstrip().startswith('#')) or (line.lstrip() == '\n'):
#         continue
#     else:
#         l.append(line)
# print(len(l))
