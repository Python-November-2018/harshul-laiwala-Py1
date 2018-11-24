from flask import Flask , redirect , render_template , session , request

app = Flask(__name__)
app.secret_key = 'thisisasecret'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter']= int(session['counter']) + 1
    else:
        session['counter'] = 1
    print('*' * 10 + str(session['counter']) + '*' * 10)
    return render_template('index.html', count = session['counter'])

@app.route('/counter', methods=["POST"])
def counter():
    print('*' * 10 + str(session['counter']) + '*' * 10)
    session['counter'] = int(session['counter']) + 2
    return redirect('/')

@app.route('/resetCounter' , methods=["POST"])
def reset_counter():
    session.clear()
    print('*' * 10 + str(session['counter']) + '*' * 10)
    return redirect('/')

@app.route('/destroy')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)