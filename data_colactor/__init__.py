from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://joao:af1235512355@localhost:5434/flask'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email_db = db.Column(db.String(150), unique=True)
    height_db = db.Column(db.Integer)

    def __init__(self, email_db, height_db):
        self.email_db = email_db
        self.height_db = height_db


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form["height_name"]
        print(email, height)
        print(type(email), type(height))
    return render_template('success.html')


if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run()
