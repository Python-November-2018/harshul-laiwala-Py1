from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkboard():
    return render_template('index.html')


@app.route('/<x>/<y>')
def user_defined_checkerboard(x,y):
    return render_template('index.html', x=int(x), y=int((int(y)/2)))

if __name__ == '__main__':
    app.run(debug=True)