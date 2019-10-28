import smtplib

#Input sender's email address and password inside quotations
#Example email address and password
senderEmail = "senderha12@gmail.com"
password = "1Q2W3e4r"

#Input the email address of the receiver(s)
receiverEmail = ["hairavelle.aguilar@guamcc.edu", "sresendez@docomopacific.com"]

def sendEmail():

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(senderEmail, password)
  
  #Type this inside "" if you want your email message to have a subject line - SUBJECT: (Title)
  #Don't forget to add "\n" just before you type in the body of your message
  #"\n" will separate your message from the subject line
	message = "SUBJECT: END OF DAY\nHaira's shift ends in 10 minutes."
  
	server.sendmail(senderEmail, receiverEmail, message)
	server.quit()

sendEmail()
