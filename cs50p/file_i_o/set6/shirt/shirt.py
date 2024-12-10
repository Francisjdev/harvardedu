import sys
from PIL import Image, ImageOps
shirt = Image.open("shirt.png")
size = shirt.size
print(size)
if len(sys.argv)<3:
    sys.exit("too few arguments")
elif len(sys.argv)>3:
    sys.exit("too many arguments")
try:
    input=Image.open(sys.argv[1])
    print(input.size)
    rinput=ImageOps.fit(input,[600,600])
    rinput.paste(shirt, (0,0), mask=shirt)
    print(type(rinput))
    rinput.save(sys.argv[2])
except FileNotFoundError:
     sys.exit("no such file")
     