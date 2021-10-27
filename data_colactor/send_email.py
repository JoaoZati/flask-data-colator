import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

from_email = os.getenv("EMAIL")
from_password = os.getenv("PASSWORD")


def send_email(email, height, avarage, count):
    to_email = email

    subject = 'Height data'
    message = f'''
    Hey there, your height is <strong>{height}</strong>.
    The average height for all collected data is <strong>{avarage}</strong>.
    Total of heights get from site is <strong>{count}</strong>!'''

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)


if __name__ == '__main__':
    send_email('joaozati@gmail.com', '182', '181', '5')
