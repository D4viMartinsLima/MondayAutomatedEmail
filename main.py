import smtplib
import datetime as dt
import random

MY_EMAIL = "addyouremail@email.com"
PASSWORD = "addyourAppPassword "

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 1:
    with open("quotes.txt", "r") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="chooseyouremail@gmail.com", msg=f"Subject: Monday Motivation\n\n{quote}")
