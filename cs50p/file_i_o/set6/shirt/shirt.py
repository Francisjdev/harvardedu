import csv, sys
if len(sys.argv)<3:
    sys.exit("too few arguments")
elif len(sys.argv)>3:
    sys.exit("too many arguments")
try:
    with open(sys.argv[1]) as in_file:
      print("lovely")
except FileNotFoundError:
     sys.exit("no such file")
     