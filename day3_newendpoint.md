task: creating a new end point 
new endpoint in your flask application “/greeting” should return “welcome to flask project”.
For example: once flask app is started I should be able to call “http://localhost:5000/greeting” and see the message in browser.

@app.route('/greeting')
def greeting():
    return 'Welcome to Flask project'
--this is what added to the code 

@app.route('/')
def hello():
    cur = mysql.connection.cursor()
    cur.execute('SELECT message FROM messages')
    messages = cur.fetchall()
    cur.close()
    return render_template('index.html', messages=messages)


--TOTAL CODE
# New endpoint to return a welcome message
@app.route('/greeting')
def greeting():
    return 'Welcome to Flask project'

@app.route('/submit', methods=['POST'])
def submit():
    new_message = request.form.get('new_message')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO messages (message) VALUES (%s)', [new_message])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
