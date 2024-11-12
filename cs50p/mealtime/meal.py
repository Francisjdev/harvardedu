
def main():
    time = input("what time is it? ")
    mealtime=convert(time)
    if mealtime >=7 and mealtime<=8:
        print("breakfast time")
    elif mealtime >=12 and mealtime <=13:
        print("Lunch time")
    elif mealtime >= 18 and mealtime <=19:
        print("dinner time")



def convert(time):
    hour, minutes = time.split(":")
    iminutes = int(minutes)
    ihour = int(hour)
    result =((ihour*60)+ iminutes)/60
    return result

main()