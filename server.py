from flask import Flask, render_template, request, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'SecretClubhousePassword'

# def validate_msg(msg, msg_location):
    # flash(msg, msg_location)
    # return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1:
        flash(u"Error: Email needs to contain at least one letter, or number and a domain.", 'errors')
        return render_template('index.html')
    if not EMAIL_REGEX.match(request.form['email']):
        flash(u"Invalid Email Address!", 'errors')
        return render_template('index.html')
    if not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        flash(u"Error: Name needs to contain at least one letter, and no numbers.", 'errors')
        return render_template('index.html')
    if len(request.form['password']) < 9:
        flash(u"Error: Passwords need to be at least 8 characters long.", 'errors')
        return render_template('index.html')
    if not request.form['password']==request.form['confirm_password']:
        flash(u"Error: Password and password confirmation need to match.", 'errors')
        return render_template('index.html')
    else:
        flash(u"Thanks for submitting your information!", 'success')
        return render_template('index.html')
    return redirect('/')

app.run(debug=True)
