with open("fuel.py") as file:
    lines = file.readlines()
    for line in lines:
        line.strip()
        print(lines)
        if line.endswith(" "):
            print("here")
