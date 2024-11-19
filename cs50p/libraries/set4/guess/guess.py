import random
lvl = int(input("intorduce a level: "))
while True:
    
    rnum = random.randint(1,lvl)
    guess= int(input("guess the number: "))
    if guess > rnum:
        print("you went  way up")
    elif guess < rnum:
        print("too low")
    else:
        print("you nailed it")
        break

print(rnum)