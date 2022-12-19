import datetime as dt
import pandas
from random import randint
import smtplib

EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

now = dt.datetime.now()
day = (now.month, now.day)

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(birthdays_row.month, birthdays_row.day): birthdays_row for (index, birthdays_row) in birthdays.iterrows()}

if day in birthdays_dict:
    letter = f"letter_templates/letter_{randint(1, 3)}.txt"
    name = birthdays_dict[day]["name"]
    email = birthdays_dict[day]["email"]

    with open(letter) as selected_letter:
        wishes = selected_letter.read()
        letter_to_send = wishes.replace("[NAME]", name)

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=email,
                                msg=f"Subject: Happy Birthday {name}!\n\n{letter_to_send}")
