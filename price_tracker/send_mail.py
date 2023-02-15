# Send notification email when the price hits below a certain level
import os
import smtplib

def send_mail(to_address, price, product, target_price, url):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    email = os.environ.get("MAIL_USER")
    password = os.environ.get("MAIL_PASS")
    server.login(email, password)
    
    subject = f"Your {product} is now available at ${price}"
    body = f"This is the moment you have been waiting for. your target is {target_price}.\nBUY NOW! {url}"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        from_addr = email,
        to_addrs= to_address,
        msg = msg
    )