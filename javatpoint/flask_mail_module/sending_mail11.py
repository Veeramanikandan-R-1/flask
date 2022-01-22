from flask import *
from flask_mail import *

app = Flask(__name__)
sender_mail_id="manirsvh98@gmail.com"
sender_mail_password="Mani123#"
receiver_mail_id_list=["r.veeramanikandany216@gmail.com",'r.veeramanikandany217@gmail.com','rsvhmani98@gmail.com']

# Flask mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = sender_mail_id
app.config['MAIL_PASSWORD'] = sender_mail_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# instantiate the Mail class
mail = Mail(app)


# configure the Message class object and send the mail from a URL
@app.route('/send_mail')
def index():
    msg = Message('subject', sender=sender_mail_id, recipients=receiver_mail_id_list)
    msg.body = 'hi, this is the mail sent by using the flask web application'
    mail.send(msg)
    return "Mail Sent, Please check the mail id"


if __name__ == '__main__':
    app.run(debug=True)