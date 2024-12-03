import sys
counter = 0
if len(sys.argv)<2:
    sys.exit("too few arguments")
elif len(sys.argv)>2:
    sys.exit("too many arguments")
try:
    with open(sys.argv[1]) as file:
    
            lines = file.readlines()
            print(len(lines))

            for s in lines:
                if s.isspace():
                    counter = counter
                else:
                    counter +=1
            print(counter)
except FileNotFoundError:
     sys.exit("no such file")

        
