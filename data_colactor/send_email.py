import smtplib
from email.mime.text import MIMEText

with open('../config.txt', 'r') as file:
    content = file.read()
    list_content = content.split('\n')
    from_email = list_content[0].replace("from_email = ", '')
    from_password = list_content[1].replace("from_password = ", '')


def send_email(email, height):
    to_email = email

    subject = 'Height data'
    message = f'Hey there, your height is <strong>{height}</strong>'

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
    send_email('joaozati@gmail.com', '182')
