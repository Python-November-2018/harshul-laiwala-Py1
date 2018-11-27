from flask import Flask , render_template , session , redirect, request , flash
import re

app = Flask(__name__)
app.secret_key = 'this is a secret key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_user_regisration():
    errors = False
    print(request.form)
    
    # All fields are required and must not be blank
    if len(str(request.form['firstName'])) < 1:
        errors=True
        flash('First Name cannot be empty', category='error')
    if len(str(request.form['lastName'])) < 1:
        errors=True
        flash('Last Name cannot be empty', category='error')
    if len(str(request.form['email'])) < 1:
        errors=True
        flash('Email cannot be empty', category='error')
    if len(str(request.form['password'])) < 1:
        errors=True
        flash('Password cannot be empty', category='error')
    if len(str(request.form['confirmPassword'])) < 1:
        errors=True
        flash('Confirm Password cannot be empty', category='error')
    
    # for keys in request.form:
    #     print('+' * 80)
    #     print(keys)
        # for key in keys:
        #     print('-'* 80)
        #     print(key)
        # if request.form[keys] == 0:
        #     flash('Cannot be empty', category= keys)
        #     errors=True
    
    # First and Last Name cannot contain any numbers
    if bool(re.search(r'\d',str(request.form['firstName']))) or bool(re.search(r'\d', str(request.form['lastName']))):
        errors=True
        flash('First and Last Name cannot contain any numbers', category='error')

    # Password should be more than 8 characters
    if len(str(request.form['password'])) <= 8:
        errors=True
        flash('Password should be more than 8 characters', category='error')
    
    # Email should be a valid email
    if bool(re.search(r'^[a-zA-Z0-9*_*.]+@[a-zA-Z0-9]+.[a-zA-z0-9]{3}$',str(request.form['email']))) == False:
        errors=True
        flash('Email should be a valid email', category='error')

    # Password and Password Confirmation should match
    if str(request.form['password']) != str(request.form['confirmPassword']):
        errors=True
        flash('Password and Password Confirmation should match', category='error')
    
    if errors == True:
        return redirect('/')
    
    flash('User Registered Successfully', category='success')
    return redirect('/')
    

    
if __name__=='__main__':
    app.run(debug=True)
