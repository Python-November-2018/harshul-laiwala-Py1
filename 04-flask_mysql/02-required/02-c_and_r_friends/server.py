from flask import Flask , render_template, redirect, session, request
from mysqlconnection import connectToMySQL

app=Flask(__name__)
app.secret_key = 'This is a a secret'
db_name = 'crfriends'

@app.route('/')
def index():
    mysql=connectToMySQL(db_name)
    query = "SELECT * from friends;"
    query_result = mysql.query_db(query)
    return render_template('index.html', friends=query_result)


@app.route('/addFriend', methods=['POST'])
def addFriend():
    print(request.form)
    mysql=connectToMySQL(db_name)
    query="INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(occupation)s,now(),now());"
    data={
        'first_name':request.form['firstName'],
        'last_name':request.form['lastName'],
        'occupation':request.form['occupation']
    }
    new_friend_record=mysql.query_db(query, data)
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)