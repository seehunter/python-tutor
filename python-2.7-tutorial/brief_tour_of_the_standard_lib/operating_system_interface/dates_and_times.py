from datetime import date

now=date.today()

# datetime.date(2003,12,2)

print now.strftime("%m-%d-%y.%d %b %Y is a %A on the %d day of %B.")

birthday=date(1964,7,31)

print birthday

age=now-birthday
print age
print age.days
