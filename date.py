from datetime import date
from dateutil.relativedelta import relativedelta


def calculate_subscription(d,months_of_subscription,cost_of_subscription_per_month):
    if months_of_subscription==1:
        cost_per_day=1000/30
        days=26
        cost_of_subscription_per_month=round(days*cost_per_day,2)
        updated_date=d+relativedelta(days=26)
        print(updated_date.strftime('%d/%m/%y'),cost_of_subscription_per_month)
    if months_of_subscription==3:
        cost_per_day=400/30
        days=89
        cost_of_subscription_per_month=round(days*cost_per_day,2)
        updated_date=d+relativedelta(days=90)
        print(updated_date.strftime('%d/%m/%Y'),cost_of_subscription_per_month)

date_components=input('Enter a Date formatted as DD/MM/YYYY : ').split('/')
year,month,day=[int(item) for item in date_components]
d=date(day,month,year)

months_of_subscription=int(input())
cost_of_subscription_per_month=int(input())


calculate_subscription(d,months_of_subscription,cost_of_subscription_per_month)