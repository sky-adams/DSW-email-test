import os
from flask import Flask, url_for, render_template, request, redirect
from flask_mail import Mail, Message
from flask_mail import Message

app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ['SENDGRID_API_KEY']
app.config['MAIL_DEFAULT_SENDER'] = os.environ['MAIL_DEFAULT_SENDER']
mail = Mail(app)

"""
mail_settings = {
    "MAIL_SERVER": os.environ['MAIL_SERVER'],
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config.update(mail_settings)
mail = Mail(app)
"""

@app.route('/', methods=['GET', 'POST'])
def renderMain():
    if request.method == 'POST' and 'message' in request.form and 'recipient' in request.form:
        """
        msg = Message('Twilio SendGrid Test Email', recipients=[request.form['recipient']])
        #msg.body = request.form['message']
        msg.html = request.form['message']
        mail.send(msg)
        """
        msg = Message('Flask-Mail test email', recipients=[request.form['recipient']])
        #msg.body = request.form['message']
        msg.html = request.form['message']
        mail.send(msg)
        print('got here')
    return render_template('home.html')
    
if __name__=="__main__":
    app.run(debug=False)
