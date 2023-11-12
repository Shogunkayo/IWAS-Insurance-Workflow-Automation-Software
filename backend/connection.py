from flask import Flask, render_template
from flask_mysqldb import MySQL
import mysql.connector

app=Flask(__name__, template_folder='C:/Users/way2wealth/Desktop/IWAS/Flask/frontend') #Change the path to the frontend folder

connection = mysql.connector.connect( host='localhost', port='3306', 
                                     user = 'root', password = 'nagag0410?', 
                                     database = 'iwas') #Password has to be changed
cur = connection.cursor()

@app.route('/')
def Home():
    #cur.execute("SELECT * FROM team")
    #fetchdata = cur.fetchall()
    #cur.close()
    #return render_template('home.html', data = fetchdata)
    pass


if __name__ == '__main__':
    app.run(debug=True)

