from flask import *
from flask_mail import *

app=Flask(__name__)

# flask mail configuration
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='rsvhmani98@gmail.com'
app.config['MAIL_PASSWORD']='Mani123#'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

# instatiate mail class
mail=Mail(app)

# use the the link and allow less secure apps to use gmail service https://www.google.com/settings/security/lesssecureapps
@app.route('/send_mail')
def send_mail_fun():
    msg=Message('checking mail flask',sender='manirsvh98@gmail.com',recipients=['r.veeramanikandany216@gmail.com'])
    msg.body='hi this is the test mail from flask'
    return 'mail sent pls check'

if __name__=="__main__":
    app.run(debug=True)