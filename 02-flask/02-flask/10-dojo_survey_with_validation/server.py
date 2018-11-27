from flask import Flask , render_template , session , redirect, request , flash

app = Flask(__name__)
app.secret_key = 'this is a secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process' , methods=['POST'])
def process_survey():
    errors = False
    if len(request.form['name']) == 0:
        flash("Name cannot be empty") 
        errors=True
    if len(str(request.form['comments'])) > 120:
        flash('Comments can only be 120 characters')
        errors = True
    if len(str(request.form['comments'])) == 0:
        flash('Comments cannot be empty')
        errors =True
    print('*'*80)
    print(request.form)
    session = {
        'name': request.form['name'],
        'dojoLocation': request.form['dojoLocation'],
        'favoriteLocation': request.form['favoriteLocation'],
        'comments':request.form['comments']
    }
    print('*' * 80)
    print(session)
    if errors == True:
        return redirect('/')
    
    return redirect('/result')

@app.route('/result')
def display_result():
    return render_template('result.html')


if __name__=='__main__':
    app.run(debug=True)
