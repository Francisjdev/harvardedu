from datetime import date
import inflect
p = inflect.engine()

def main():
    year, month, day=input("bday(YYYY-MM-DD): ").split("-")
    bday = date(int(year), int(month),int(day))
    get_minutes(bday)
    

def get_minutes(udate):
    days = (date.today()-udate)
    minutes = days.days *24*60
    words=p.number_to_words(minutes, andword="")
    print(f"{words} minutes")



...


if __name__ == "__main__":
    main()
