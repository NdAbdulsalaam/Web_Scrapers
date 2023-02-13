# Send notification email when the price hits below a certain level
import os
import smtplib

def send_mail(to_address, price, product):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    email = os.environ.get("MAIL_USER")
    password = os.environ.get("MAIL_PASS")
    server.login(email, password)
    
    subject = f"Your {product} is now available at ${price}"
    body = "This is the moment we have been waiting for. your target is {target_price}.\nclick here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        from_addr = email,
        to_addrs= to_address,
        msg = msg
    )
    