import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_user = os.environ.get("MYSQL_USER", "")
db_pass = os.environ.get("MYSQL_PASSWORD", "")
db_name = os.environ.get("MYSQL_DB", "")
db_uri = "mysql+mysqldb://{user}:{passwd}@db/{name}".format(
    user=db_user, passwd=db_pass, name=db_name,
)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return '<User %s>' % self.name


@app.route('/')
def index():
    num_users = User.query.count()
    return "There are {num} users in the database".format(num=num_users)

if __name__ == "__main__":
    app.run()
