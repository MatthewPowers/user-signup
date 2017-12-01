from flask import Flask, request, redirect, render_template
import cgi
#import os
#import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signin.html')


@app.route("/validat_login", methods=['POST'])
def validate_input():

    password = request.form["password"]
    user_name = request.form["user_name"]
    verify_Password = request.form["verify_Password"]
    email = request.form["email"]

    user_name_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    error = 0
    sym = 0

    if len(user_name) < 4 or len(user_name) > 20:
        user_name_error = "Not a valid user name"
        error = error + 1
    else:
        user_name_error = ''

    for char in user_name:
        if char == ' ':
            user_name_error = "Not a valid user name"
            error = error + 1

    if len(password) < 4 or len(password) > 20:
        password_error = "Not a valid password"
        error = error + 1
    else:
        password_error = ''

    for char in password:
        if char == ' ':
            password_error = "Not a valid password"
            error = error + 1

    if verify_Password != password:
        verify_error = 'password does not match'
        error = error + 1
    else:
        verify_error = ''

    for char in email:
        if char == '@' or char == '.':
            sym = sym + 1

    if len(email) < 4 or len(email) > 20 or sym != 2:
        email_error = 'that is not a valid email'
    else:
        email_error = ''
        

    if error == 0:
        return render_template('valid_signin.html', user_name=user_name)

    else:
        return render_template('signin.html', user_name=user_name, email=email, password_error=password_error, user_name_error=user_name_error, 
            verify_error=verify_error, email_error=email_error)

app.run()