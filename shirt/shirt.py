import sys, os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file1, file2 = sys.argv[1], sys.argv[2]
ext1, ext2 = os.path.splitext(file1)[1].lower(), os.path.splitext(file2)[1].lower()
if ext1 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
elif ext2 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
elif ext1 != ext2:
    sys.exit("Input and output have different extensions")
elif not os.path.exists(sys.argv[1]):
    sys.exit("Input does not exist")

with Image.open("shirt.png") as shirt:
    with Image.open(sys.argv[1]) as image:
        image = ImageOps.fit(image, shirt.size)
        image.paste(shirt, shirt)
        image.save(sys.argv[2])