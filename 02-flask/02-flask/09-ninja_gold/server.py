from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'ThisIsASecret'

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)