from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mNoWF5rUjZPyNNScRAw6sPjmZnP87rAQkuM7WAhbRM'
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

        data = Data.query.filter_by(email_db=email).first()
        # data = db.session.query(Data).filter(Data.email_db == email).count() # should return 0

        if data:
            flash('Email already exists', category='error')
            return redirect(url_for('home'))

        send_email(email, height)
        data = Data(email, height)
        db.session.add(data)
        db.session.commit()
        flash("Email successfully sent", category='success') # can pass like a render in text

    return render_template('success.html')


if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run()
