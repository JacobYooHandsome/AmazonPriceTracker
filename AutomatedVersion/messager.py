from email.message import EmailMessage
import ssl, smtplib
from dotenv import load_dotenv

load_dotenv()

class Messager():
    def __init__(self):
        self.from_email = "<from email>"
        self.to_email = "<to email>"
        self.app_pass = "<app password>"
    
    def send_email(self, product, old_price, new_price):
        em = EmailMessage()
        em["From"] = self.from_email
        em["To"] = self.to_email
        em["Subject"] = f"DEAL FOR {product} ON PLUGIN BOUTIQUE WAS ${old_price} AND NOW IS ${new_price}!"
        em.set_content(f"Dear Me,\n\nThe current price of {product} used to be ${old_price} and is now ${new_price}!\n\nFrom,\n\n Me")

        context = ssl.create_default_context() # secures the message!
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.from_email, self.app_pass)
            smtp.sendmail(self.from_email, self.to_email, em.as_string())
