from flask import *
from flask_mail import *
from random import randint

app = Flask(__name__)
sender_mail_id="manirsvh98@gmail.com"
sender_mail_password="Mani123#"
receiver_mail_id_list=["r.veeramanikandany216@gmail.com",'r.veeramanikandany217@gmail.com','rsvhmani98@gmail.com']
otp=randint(000000,999999)

# Flask mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = sender_mail_id
app.config['MAIL_PASSWORD'] = sender_mail_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# instantiate the Mail class
mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/verify',methods=['POST'])
def verify_fun():
    email=request.form['email']
    msg = Message('OTP for verification', sender=sender_mail_id, recipients=[email])
    msg.body = "OTP for email verification is {}".format(otp)
    mail.send(msg)
    return render_template("verify.html",email=email)

@app.route('/validate',methods=["POST"])
def validate_fun():
    user_otp=request.form['otp_entered']
    if otp==int(user_otp):
        return "<h3>Email verified successfully</h3>"
    return "<h3>failure</h3>"

    # configure the Message class object and send the mail from a URL
@app.route('/send_mail')
def sendmail():
    msg = Message('subject', sender=sender_mail_id, recipients=receiver_mail_id_list)
    msg.body = 'hi, this is the mail sent by using the flask web application'
    mail.send(msg)
    return "Mail Sent, Please check the mail id"


if __name__ == '__main__':
    app.run(debug=True)