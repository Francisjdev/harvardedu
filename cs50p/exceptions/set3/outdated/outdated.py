def date_checker(date,arr):
        if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year= int(year)
                if month>0 and month <13 and day<32 and day>0:
                    print(f"{year}-{month:02}-{day:02}")
                else:
                    date = input("introduce a date in MM/DD/YYYY:  ")
                    date_checker(date)
        elif "," in udate:
            month, day, year = udate.replace(","," ").split()
            day = int(day)
            year= int(year)
            monthidx = arr.index(month.capitalize())
            if   int(day)<32 and int(day)>0:
                    print(f"{year}-{monthidx+1:02}-{day:02}")
            else:
                    date = input("introduce a date in MM/DD/YYYY:  ")
                    date_checker(date,arr)
year =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
        try:
            udate = input("introduce a date in MM/DD/YYYY: \n ")
            date_checker(udate,year)
          
        except EOFError:
            break



    

     