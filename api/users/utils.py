import smtplib
from email.message import EmailMessage

def send_email(subject, body, recipient):
    try:
        email = EmailMessage()
        email['Subject'] = subject
        email['From'] = 'dinhhuyfpt09@gmail.com'  # Replace with your sender email address
        email['To'] = recipient
        email.set_content(body)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # Replace with your SMTP server and port
            smtp.starttls()  # Enable TLS encryption
            smtp.login('dinhhuyfpt09@gmail.com', 'ccyy ydbi oqbe olsj')  # Replace with your email credentials
            smtp.send_message(email)

        return 'Email sent successfully!'
    except Exception as e:
        return f'Failed to send email. Error: {str(e)}'
