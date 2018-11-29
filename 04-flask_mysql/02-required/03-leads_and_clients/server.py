from flask import Flask, redirect, session, request, render_template

app=Flask(__name__)
db_name='lead_gen_business'

@app.route('/')
def display_dashboard():
    return render_template('index.html')

@app.route('/apply_filter', methods=['POST'])
def filter_results():
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)