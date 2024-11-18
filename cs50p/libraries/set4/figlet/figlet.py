from pyfiglet import Figlet
import sys, random
figlet = Figlet()
leng=len(figlet.getFonts())
if len(sys.argv)==3:
    if sys.argv[1] == "-f" or sys.argv[1]== "--font":
        f=sys.argv[2]
        figlet.setFont(font=f)
        s= input("input: ")
        print(figlet.renderText(s))
    else:
        sys.exit("Invalid Usage")
elif len(sys.argv)==1:
    ind=random.randrange(leng)
    arr= figlet.getFonts()
    figlet.setFont(font=arr[ind])
    s= input("input: ")
    print(figlet.renderText(s))
    
   



