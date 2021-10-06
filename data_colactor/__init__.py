from flask import Flask, render_template, request, url_for

app = Flask(__name__)


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
    app.debug = True
    app.run()
