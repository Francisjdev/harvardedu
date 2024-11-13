groceries={}
while True:
    try:
        item = input("what is missing from the fridge? ").upper()
        if item in  groceries:
            groceries[item]+=1
        else:
            groceries[item]=1


    except EOFError:
        ordr_groceries =dict(sorted(groceries.items()))
        for key ,value in ordr_groceries.items():
            print(f"{value} {key}")
        
        break
