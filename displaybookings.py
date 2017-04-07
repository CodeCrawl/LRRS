from flask import render_template,request,session
from App import app
from App import mysql

@app.route('/displaybookings',methods=['POST'])
def displaybooking():
    _uname = session.get('uname')
    conn = mysql.connect()
    curr = conn.cursor()
    curr.execute("call sp_displaybooking(%s)",(_uname))
    display = curr.fetchall()
    if session.get('logged_in'):
        return render_template('displaymybooking.html',display=display)
    else:
        return render_template("pleaseloginfirst.html")