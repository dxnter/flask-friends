from flask import Flask, request, redirect, render_template, session, flash, url_for
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')
@app.route('/')
def index():
    query = "SELECT * FROM friends_full"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends_full (name, age, friends_since, created_at, updated_at) VALUES (:name, :age, DATE_FORMAT(NOW(), '%M %D %Y'), NOW(), NOW())"
    data = {
             'name': request.form['name'],
             'age':  request.form['age']
           }

    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
