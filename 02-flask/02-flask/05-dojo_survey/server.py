from flask import Flask, render_template,redirect,request,session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/danger')
def danger():
    print('*'* 50 + ' a user tried to visit /danger.  we have redirected the user to "/" ' + '*'* 50)
    return redirect('/')

@app.route('/process', methods=['POST'])
def process_survey_form():
    # survey_info ={
    #     'name': request.form['name'],
    #     'favoriteLanguage':request.form['favoriteLanguage'],
    #     'dojoLocation': request.form['dojoLocation'],
    #     'comments': request.form['comments']
    # }
    # print(survey_info)
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)