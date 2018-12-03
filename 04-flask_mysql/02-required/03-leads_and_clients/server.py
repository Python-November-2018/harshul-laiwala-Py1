from flask import Flask, redirect, session, request, render_template , flash
from mysqlconnection import connectToMySQL

app=Flask(__name__)
app.secret_key='this is a secret'
db_name='lead_gen_business'

@app.route('/')
def display_dashboard():
    print(session)
    mysql = connectToMySQL(db_name)
    if 'from_date' in session:
        if 'to_date' in session:
            query = """SELECT concat(clients.first_name,' ',clients.last_name) as client_name , count(leads.leads_id) as number_of_leads FROM clients
 JOIN sites ON clients.client_id = sites.client_id 
 JOIN leads ON sites.site_id = leads.site_id 
 WHERE leads.registered_datetime BETWEEN %(from_date)s and %(to_date)s GROUP BY clients.client_id;"""
            data = {
                'from_date':session['from_date'],
                'to_date':session['to_date']
            }
            query_result = mysql.query_db(query, data=data)
            return render_template('index.html',query_result=query_result)
        else:
            flash('')
    else:
        flash('')
        query = """SELECT concat(clients.first_name,' ',clients.last_name) as client_name , count(leads.leads_id) as number_of_leads FROM clients
JOIN sites ON clients.client_id = sites.client_id 
JOIN leads ON sites.site_id = leads.site_id 
GROUP BY clients.client_id;"""
        query_result = mysql.query_db(query)
        print(query_result)
        return render_template('index.html', query_result=query_result)

@app.route('/apply_filter', methods=['POST'])
def filter_results():
    # print('*' * 80)
    # print(request.form)
    # session={
    #     'from_date':request.form['from_date'],
    #     'to_date':request.form['to_date']       
    # }
    session['from_date']=request.form['from_date']
    session['to_date']=request.form['to_date']     

    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)