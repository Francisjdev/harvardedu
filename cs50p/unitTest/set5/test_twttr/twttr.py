def main():
    
    str = input("word: ")
    print(shorten(str) )


def shorten(word):
    word = word.lower()
    vwls=["a","e","i","o","u"]
    nwwrd =""
    for letter in word:
        if letter not in vwls:
            nwwrd += letter
    return nwwrd

if __name__ == "__main__":
    main()