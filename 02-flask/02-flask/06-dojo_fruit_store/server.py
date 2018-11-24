from flask import Flask, render_template, request, redirect
from datetime import datetime 

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    total_items = int(request.form['strawberry'])+ int(request.form['raspberry']) + int(request.form['apple'])
    # strawberry_quantity = int(request.form['strawberry'])
    # raspberry_quantity = int(request.form['raspberry'])
    # apples_queantity  = int(request.form['apple'])
    return render_template("checkout.html", form_data=request.form , total= total_items , current_time=datetime.now())

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    