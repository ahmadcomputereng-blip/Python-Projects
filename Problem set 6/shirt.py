import sys
from PIL import Image ,ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not(sys.argv[2].endswith(".jpg")) and not(sys.argv[2].endswith(".png")):
    sys.exit("Invalid output")
elif (sys.argv[1][-4:]) != (sys.argv[2][-4:]):
    sys.exit("Input and output have different extensions")

try:
    with Image.open(sys.argv[1]) as img , Image.open("shirt.png") as shirt:
        size = shirt.size
        photo = ImageOps.fit(img , size)
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
