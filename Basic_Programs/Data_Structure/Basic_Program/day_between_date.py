from datetime import date

while True:
    first_date=str(input("enter first date in /yyyy/mm/dd format: "))
    last_date=str(input("enter last date in /yyyy/mm/dd format: "))
    date_list=[first_date.split("/"),last_date("/")]
    if(len(date_list[0])==3 and len(date_list[1])==3):
        if()
f_date = date(2014, 7, 2)
f_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
