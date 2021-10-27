from data_colactor import db
from data_colactor.models import Data
from data_colactor.send_email import send_email
from flask import render_template, request, url_for, redirect, flash, Blueprint
from sqlalchemy.sql import func


views = Blueprint('views', __name__, )


@views.route('/')
@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@views.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form["height_name"]

        data = Data.query.filter_by(email_db=email).first()
        # data = db.session.query(Data).filter(Data.email_db == email).count() # should return 0

        if data:
            flash('Email already exists', category='error')
            return redirect(url_for('views.home'))

        data = Data(email, height)
        db.session.add(data)
        db.session.commit()
        avarange_weight = db.session.query(func.avg(Data.height_db)).scalar()
        avarange_weight = round(avarange_weight, 2)
        count = db.session.query(Data.height_db).count()
        send_email(email, height, avarange_weight, count)
        flash("Email successfully sent", category='success')  # can pass like a render in text

    return render_template('success.html')
