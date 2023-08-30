import time

import yagmail
import pandas
import datetime
from news import NewsFeed


def send_email():
    for index, row in df.iterrows():
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.datetime.now() - datetime.timedelta(
            days=1)).strftime("%Y-%m-%d")
        newsfeed = NewsFeed(interest=row['interest'],
                            from_date=yesterday,
                            to_date=today)
        email = yagmail.SMTP(user="email",
                             password="password")
        email.send(to=row["email"],
                   subject=f"Your {row['interest']} news for today!",
                   contents=f"Hi {row['name']}\n see what's the latest on {row['interesr']}"
                            f"\n {newsfeed.get()}",
                   attachments="design.txt")


while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 45:
        df = pandas.read_excel("people.xlsx")

        send_email()
    time.sleep(60)

