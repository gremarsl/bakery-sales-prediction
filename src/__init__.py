
import datetime

def main():
    print("Main")
    getWeekday()

def getWeekday():
    #Return the day of the week as an integer, where Monday is 0 and Sunday is 6.

    date=datetime.datetime.today()
    print(date)
    today= datetime.datetime.today().weekday()
    print(today)
    todayInWord=datetime.datetime.today().strftime('%A')
    print(todayInWord)

if __name__ == "__main__":
    main()
