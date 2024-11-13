fuel = input("how much fuel we got left? ")
num, div = fuel.split("/")

if num < div:
    try:
        result = int(num)/int(div)
        result=round(result*100)
        print (f"{result}%")
    except (ValueError, ZeroDivisionError):
        print("there is something wrong")
try:
        result = int(num)/int(div)
        result=round(result*100)
        print (f"{result}%")
except (ValueError, ZeroDivisionError):
        print("there is something wrong")


    