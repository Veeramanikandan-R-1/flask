from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flask_blog import db, bcrypt
from flask_blog.models import User, Post
from flask_blog.users.forms import (Registration_form, Login_form, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flask_blog.users.utils import save_picture, send_reset_email

users=Blueprint('users',__name__)#creating instance / object by passing name and blueprint

@users.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = Registration_form() #creating instance
    if form.validate_on_submit():
        # to hash a password
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8') #utf-8 to get only string in decoded value
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        # sending user info to db
        db.session.add(user)
        # to save changes
        db.session.commit()
        flash(f'Account created for {form.username.data} and now you are able to login!','success')
        # to redirect to login page
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = Login_form() #creating instance
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("main.home"))

        # not meeting condition invalid username or pwd
        else:
            flash('Invalid credentials. Please check email or password','danger ')
    return render_template('login.html', title='login', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))


@users.route("/account",methods=['GET','POST'])
# to secure the account page using login
@login_required
def account():
    form=UpdateAccountForm() #creating instance for update form
    # validating to update username and pwd
    if form.validate_on_submit():
        if form.picture.data:
            picture_file=save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash("Your account has been updated","success")
        return redirect(url_for("users.account")) #used redirect to avoid another post request on clicking reload button
    elif request.method=="GET":
        form.username.data=current_user.username
        form.email.data = current_user.email
    image_file= url_for("static",filename="profile_pic/"+current_user.image_file)
    return render_template('account.html',title="Account",image_file=image_file,form=form) #image file returned to template



# creating route to display only post by specific users in home page
@users.route("/user/<string:username>")
def user_posts(username):
    page=request.args.get('page',1,type=int)
    user=User.query.filter_by(username=username).first_or_404()
    posts=Post.query.filter_by(author=user)\
            .order_by(Post.date_posted.desc())\
                .paginate(page=page,per_page=5)
    return render_template('user_posts.html',posts=posts,user=user)


@users.route("/reset_password" ,methods=['GET','POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form=RequestResetForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instruction to reset password.','info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html',title="Reset Password", form=form)

@users.route("/reset_password/<token>" ,methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    user=User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token",'warning')
        return redirect(url_for('users.reset_request'))
    form=ResetPasswordForm()
    if form.validate_on_submit():
        # to hash a password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            'utf-8')  # utf-8 to get only string in decoded value
        # sending user info to db
        user.password=hashed_password
        # to save changes
        db.session.commit()
        flash(f'your password was updated and now you are able to login!', 'success')
        # to redirect to login page
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title="Reset Password", form=form)