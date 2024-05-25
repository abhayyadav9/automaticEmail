import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule

def send_email():
    # Email account credentials
    email = "abhay.202204097@tulas.edu.in"
    password = "202204097"
    to_email = "bickyyadav404@gmail.com"

    # Email content
    subject = "hack"
    body = "Your email is hacked."

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(email, password)

        # Send the email multiple times
        for i in range(50):
            text = msg.as_string()
            server.sendmail(email, to_email, text)

        # Close the server connection
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the job daily at a specific time
schedule.every().day.at("18:30").do(send_email)

# Run the job immediately
send_email()

# Keep the script running to execute scheduled jobs
while True:
    schedule.run_pending()








#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import os
# import schedule
# import time
#
# def send_email():
#     # Email account credentials from environment variables
#     email = os.getenv("EMAIL_USER")
#     password = os.getenv("EMAIL_PASS")
#     to_email = "yadavabhay8227@gmail.com"
#
#     # Email content
#     subject = "Daily Report"
#     body = "This is your daily report."
#
#     # Set up the MIME
#     msg = MIMEMultipart()
#     msg['From'] = email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#
#     # Attach the body with the msg instance
#     msg.attach(MIMEText(body, 'plain'))
#
#     try:
#         # Set up the server
#         server = smtplib.SMTP('smtp.gmail.com:587')
#         server.starttls()
#         server.login(email, password)
#
#         # Send the email
#         text = msg.as_string()
#         server.sendmail(email, to_email, text)
#
#         # Close the server connection
#         server.quit()
#         print("Email sent successfully.")
#     except Exception as e:
#         print(f"Failed to send email: {e}")
#
#
#
# if __name__ == "__main__":
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
