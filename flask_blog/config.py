import os

class Config:
    # secret key
    SECRET_KEY='67e30547f37df0b4bfd158ab4deee457'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER= 'smtp.googlemail.com'
    # app.config['MAIL_PORT']=465

    MAIL_PORT=587
    MAIL_USE_TLS=True
    # make all the above variable as env variable if needed particulary for db info such as username and password
    MAIL_USERNAME=os.environ.get('EMAIL_USER')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
# app.config['MAIL_USERNAME']='r.veeramanikandany216@gmail.com'
# app.config['MAIL_PASSWORD']='Mani321#'