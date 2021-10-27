from flask import Flask, render_template, request, url_for, redirect, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mNoWF5rUjZPyNNScRAw6sPjmZnP87rAQkuM7WAhbRM'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://joao:af1235512355@localhost:5434/flaskdatacolector'
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
    global file
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            flash('Empty file', 'error')
            return redirect(url_for('home'))
        file.save(secure_filename(f'uploaded_{file.filename}'))
        with open(f'uploaded_{file.filename}', 'a') as f:
            f.write('This was add later')
        flash('Upload successfully send', 'success')
        return render_template('home.html', btn=True)
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_file(f'uploaded_{file.filename}', attachment_filename=f'yourfile_{file.filename}', as_attachment=True)


if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run()
