import flask
import mysql.connector
import config

app = flask.Flask(__name__)

myexample_db = mysql.connector.connect(
    host = "localhost",
    user = config.username,
    password = config.password
)

mycursor = myexample_db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase;")
mycursor.execute("USE mydatabase;")
mycursor.execute("CREATE TABLE IF NOT EXISTS friends (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), major VARCHAR(255), age INT);")
myexample_db.commit()

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '3306'))
    except ValueError:
        PORT = 3306
    app.run(HOST, PORT)