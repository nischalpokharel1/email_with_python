import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587) #port for tsl 
smtp_object.ehlo() #start server
smtp_object.starttls()
# password = getpass.getpass('Password please: ')
email = getpass.getpass('Email: ')
password = getpass.getpass('password: ')
smtp_object.login(email,password)
from_address = email
to_address = ['pokharelnischal456@gmail.com', 'birajraut@gmail.com', 'nischalpokharel@bajratechnologies.com']
subject = input('enter the subject: ')
message = input('enter the message: ')
msg = "Subject: "+subject+'\n'+message
smtp_object.sendmail(from_address,to_address,msg)

# pokharelnischal567@gmail.com
# uzgffsgeqbzrcxtv

print('hello')
