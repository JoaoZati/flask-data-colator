from data_colactor import create_app, db

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
    db.create_all(app=create_app())
