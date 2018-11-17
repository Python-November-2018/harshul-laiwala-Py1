from flask import Flask, render_template,redirect,request,session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_survey_form():
    print(request.form)
    survey_info = (

    )
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)