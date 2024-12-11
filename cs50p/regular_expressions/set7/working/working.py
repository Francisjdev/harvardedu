import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    checked= re.search(r"(1?[0-9]:?[0-5]?[0-9]?) (am|pm) to (1?[0-9]:?[0-5]?[0-9]?) (am|pm)",s, re.IGNORECASE)
    holder = list(checked.groups())
    timeband= {
        "1":"13",
        "2":"14",
        "3":"15",
        "4":"16",
        "5":"17",
        "6":"18",
        "7":"19",
        "8":"20",
        "9":'21',
        "10":'22',
        "11":"23",
        "12":"00",
    }
    for part in range(len(holder)):
        if holder[part].isnumeric():
            print(type(part))
            print(holder[part])
            if ":" in holder[part]:
                print("im here")
                shift = holder[part].split(":")
                hour = int(shift[0])*60+int(shift[1])
                hour = hour/60
                if hour >12:
                    return "invalid time"
            elif int(holder[part]) > 12:
                return "invalid time"
        if holder[part] == 'pm':
            if ":" in holder[part-1]:
                hour, minutes = holder[part-1].split(":")
                hour = timeband[hour]
                holder[part-1] = hour + ":" + minutes
                print(holder[part-1])
    print(holder)
 

if __name__ == "__main__":
    main()
