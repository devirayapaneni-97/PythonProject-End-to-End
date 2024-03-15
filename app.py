import os
from flask import Flask, render_template, request, redirect, url_for
import psycopg2

# Declare flask app
app = Flask(__name__,template_folder='templates')

# Initialize MySQL
#mysql = MySQL(app)

#initialize postgres connection

conn = psycopg2.connect(database="achievers",user="flaskdevl",password="flaskdevl01",host="dev-achievers-01.cdcue0e6sf3u.us-east-1.rds.amazonaws.com",port="5432")
@app.route('/')
def hello():
    cur = conn.cursor()
    cur.execute('SELECT message FROM dbo.messages')
    messages = cur.fetchall()
    cur.close()
    return render_template('index.html', messages=messages)


@app.route('/submit', methods=['POST'])
def submit():
    new_message = request.form.get('new_message')
    cur = conn.cursor()
    cur.execute('INSERT INTO dbo.messages (message) VALUES (%s)', [new_message])
    conn.commit()
    cur.close()
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
