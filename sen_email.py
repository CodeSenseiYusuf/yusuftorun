from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Gmail hesabınıza giriş yapın
    gmail_user = 'your_email@gmail.com'
    gmail_password = 'your_password'
    
    # E-posta bilgilerini ayarlayın
    subject = 'New Message from Portfolio Website'
    body = f"""
    Name: {name}
    Email: {email}
    
    Message:
    {message}
    """

    # E-posta oluşturun
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = 'your_email@gmail.com'
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # SMTP sunucusuna bağlanın ve e-postayı gönderin
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, 'your_email@gmail.com', msg.as_string())
        server.close()
        return 'Email sent successfully!'
    except Exception as e:
        return f'Error occurred: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
