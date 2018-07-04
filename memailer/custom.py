from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
username = "thebiznis@gmail.com"
password = "8532thebiznis"
from_email = username
to_list = ["hungrypy@gmail.com", "mateoholman@gmail.com"]
msg_greeting = "Hello there, this is a test e-mail"

SMTP = SMTP(host, port)
SMTP.ehlo()
SMTP.starttls()
try:
    SMTP.login(username, password)
    SMTP.sendmail(from_email, to_list, msg_greeting)
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("An error occured")
SMTP.quit()