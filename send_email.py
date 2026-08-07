import smtplib, ssl


def send_email(user_email, message, subject):
    host = "smtp.gmail.com"
    port = 465

    username = "generalmrabdulloh@gmail.com"
    password = "svnk nndv eion aidx"

    receiver = "generalmrabdulloh@gmail.com"
    context = ssl.create_default_context()

    message = f"Subject: {subject}\n{user_email}\n\n{message}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


#send_email()