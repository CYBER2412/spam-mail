import smtplib

times = input("how many times do you want to spam? > ")

fromaddr = input("from what email do you want to spam? > ")
toaddrs = input("to what email do you want to spam > ")
msg = input("what do you want to spam to ", toaddrs)
password = input("what is the password from ", fromaddr)

for x in range(times):

    def send_mail():
        username = fromaddr
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

    send_mail()