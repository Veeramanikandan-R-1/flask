import os
import secrets
from PIL import Image
from flask import url_for,current_app
from flask_mail import Message
from flask_blog import mail
# to contain additional file for users

def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_picture.filename) #_underscore is used as variable to throw away at future
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(current_app.root_path,'static/profile_pic',picture_fn)

    # resizing picture using pillow module to speed up website
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token=user.get_reset_token()
    msg=Message("Password Reset Request",sender='r.veeramanikandany216@gmail.com',recipients=[user.email])#body
    # body uses f string as multiline """ use only for python greater than 3.6"""
    # external is true used for using absolute link not relative link and use only {} single brace not double
    # to don't leave any gap at front'
    msg.body=f'''To reset your password visit the following link
{url_for('users.reset_token',token=token,_external=True)}

If you do not make this request, kindly ignore the message
'''
    mail.send(msg)