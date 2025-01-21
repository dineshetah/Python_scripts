How Does Email Work ? 
SMTP means Simple MAil Transfer Protocol 

import smtplib

my_email = "dinesh.etah457@gmail.com"
password = "rsogimolfaikckyb"
#connection = smtplib.SMTP("smtp.gmail.com")      # here create a object SMTP class
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()     # TLS stands for  Transport Layer Security 
    connection.login(user=my_email, password= password)
    connection.sendmail(
        from_addr= my_email, 
        to_addrs="sudeepyadav19082019@gmail.com", 
        msg ="Subject:Hello\n\nThis is the body of my email.")
#connection.close()


# Working with the datatime Module
import datetime as dt  # why? for current date time  

currnt = dt.datetime.now()
year = currnt.year
month = currnt.month
day_of_week = currnt.weekday()
dt_of_birth = dt.datetime(year=1993, month=7, day=15)
print(year)
print(type(year))
print(type(currnt))
print(month)
print(day_of_week)
print(dt_of_birth)