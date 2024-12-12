import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    s = s.replace(",", " ").lower()
    s= s.split()
    couter = 0
    for word in s:
        if re.search(r"^um$",word):
            couter += 1
    print(couter)



...


if __name__ == "__main__":
    main()
