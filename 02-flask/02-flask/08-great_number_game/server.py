from flask import Flask , render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'ThisisSecret'

@app.route('/')
def displayApp():
    if 'number' not in session:
        session['number'] = random.randint(0,101)
        print(session['number'])
    return render_template('index.html')

@app.route('/process' , methods=['POST'])
def processNumber():
    print(request.form)
    if int(request.form['inputNumber']) > session['number']:
        session['display'] = 'high'
    elif int(request.form['inputNumber']) < session['number']:
        session['display'] = 'low'
    else:
        session['display'] ='match'   
    print(session)
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)