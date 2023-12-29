import smtplib as s
ob = s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("1pratham1sharma@gmail.com","thecasuals")
subject = "sending email using python"
body = "hello,pratham"
message ="Subject:{}\n\n{}".format(subject,body)
listofaddress = ["1pratham1sharma@gmail.com","ranshsoni1234@gmail.com","shivadantare@gmail.com"]
ob.sendmail("1pratham1sharma",listofaddress,message)
print("mail sent successfully")
ob.quit()

# MAIL_MAILER=smtp
# MAIL_HOST=smtp.gmail.com
# MAIL_PORT=587
# MAIL_USERNAME=null
# MAIL_PASSWORD=null
# MAIL_ENCRYPTION=tls