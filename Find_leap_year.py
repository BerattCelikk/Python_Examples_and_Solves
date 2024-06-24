#  PROGRAM THAT FINDS LEAP YEARS.((LEAP YEAR % 4==0)  and (LEAP YEAR % 400 == 0) and (LEAP YEAR % 100 != 0))


year=int(input("enter a year : "))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} isn't a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} isn't a leap year")