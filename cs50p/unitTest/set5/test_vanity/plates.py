def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numpart=""
    if 1 < len(s) < 7:
        start=s[0:2]
        if start.isalpha():
            
            i=3
            for i in range(len(s)):
                if s[i].isnumeric():
                    if s[i]=="0" and s[i-1].isalpha():
                        return False
                    numpart +=s[i] 
                   
            print (numpart)
            return True
    return False


if __name__ == "__main__":
    main()