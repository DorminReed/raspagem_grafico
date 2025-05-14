import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, sender_email, sender_passowrd, recipient_email):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_passowrd)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Falha ao enviar email: {e}")