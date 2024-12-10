import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    unchecked = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip)
    splitted= re.split(r'\.+', unchecked.group(0))
    for section in splitted:
        if int(section)>255:
            sys.exit("invalid IP")
        else:
            return "Valid ip"

   
...


if __name__ == "__main__":
    main()
