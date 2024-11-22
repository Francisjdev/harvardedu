
import inflect 
p = inflect.engine()
names=[]
while True:
    try:
        names.append(input("Write a name: "))
       
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")
        break
    