
# email_sender using Python


from dotenv import load_dotenv
import smtplib
import os

load_dotenv()




userEmail = os.getenv("USER")
password = os.getenv("DATABASE_URL")
recipient = os.getenv("DEBUG")


sender_email = userEmail  # Replace with your Gmail email address
sender_password = password  # Replace with your Gmail password

message_template = "Hello {name}, I hope this message finds you well.\nNote that this message is sent by a script using Python."

names = ["Alice", "Bob", "Charlie", "John"]  # Replace with the names of your recipients
for name in names:
    message = message_template.format(name=name)
    recipient_email = recipient  # Replace with the recipient's email address

    # Establish a secure connection with the SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message)
