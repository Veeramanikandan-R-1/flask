from flask import *
from flask_mail import *

app=Flask(__name__)
sender_mail_id="manirsvh98@gmail.com"
sender_mail_password="Mani123#"
receiver_mail_id_list=["r.veeramanikandany216@gmail.com",'r.veeramanikandany217@gmail.com','rsvhmani98@gmail.com']

# flask mail configuration
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='manirsvh98@gmail.com'
app.config['MAIL_PASSWORD']='Mani123#'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

# instatiate mail class
mail=Mail(app)

# use the the link and allow less secure apps to use gmail service https://www.google.com/settings/security/lesssecureapps
@app.route('/send_mail')
def send_mail_fun():
    with mail.connect() as conn:
        for user in receiver_mail_id_list:
            with app.open_resource("C:\\Users\\USER\\Downloads\\retrofit_amz_024.png") as fp:
                msg=Message('checking attach facility flask',sender='manirsvh98@gmail.com',recipients=[user])
                msg.body='hi this is the test mail from flask'
                msg.attach("retrofit_amz_024.png","retrofit_amz_024/png",fp.read())
            conn.send(msg)
    return 'sent'

if __name__=="__main__":
    app.run(debug=True)