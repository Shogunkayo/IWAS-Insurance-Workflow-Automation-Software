from flask import Flask
# from flask_mysqldb import MySQL
# import mysql.connector

app = Flask(__name__)

'''
connection = mysql.connector.connect( host='localhost', port='3306', 
                                     user = 'root', password = 'password123', 
                                     database = 'iwas') #Password has to be changed
cur = connection.cursor()
'''


@app.route('/')
def root():
    return "<p>Hello There</p>"

if __name__ == '__main__':
    app.run(debug=True)

