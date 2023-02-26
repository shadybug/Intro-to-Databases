import flask
import mysql.connector
import config

app = flask.Flask(__name__)

myexample_db = mysql.connector.connect(
    host = "localhost",
    user = config.username,
    password = config.password
)

# Database setup

mycursor = myexample_db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase;")
mycursor.execute("USE mydatabase;")
mycursor.execute("CREATE TABLE IF NOT EXISTS friends (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), major VARCHAR(255), age INT);")

sql = "INSERT INTO friends (name, major, age) VALUES (%s, %s, %s)"
value = [ ("Harry", "Astrophysics", 21), ("Laura", "Computer Science", 19), ("Peter", "Art", 17), ("Amy", "Chemistry", 26) ]

mycursor.executemany(sql, value)

myexample_db.commit()

@app.route('/')
def hello():
    # Select data from the database

    sql = "SELECT name,major,age FROM friends"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return flask.render_template("friends.html", list=myresult, title="All Friends")

@app.route('/olderfriends')
def olderfriends():
    # Select data from the database

    sql = "SELECT name,major,age FROM friends WHERE age > 20"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return flask.render_template("friends.html", list=myresult, title="Friends Over 20")

@app.route('/youngerfriends')
def youngerfriends():
    # Select data from the database

    sql = "SELECT name,major,age FROM friends WHERE age < 20"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return flask.render_template("friends.html", list=myresult, title="Friends Under 20")

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '3306'))
    except ValueError:
        PORT = 3306
    app.run(HOST, PORT)