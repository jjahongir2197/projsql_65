from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///analytics.db'
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(100))

with app.app_context():
    db.create_all()

    db.session.add_all([
        Visit(page="home"),
        Visit(page="home"),
        Visit(page="about")
    ])
    db.session.commit()

    result = db.session.query(
        Visit.page,
        func.count(Visit.id)
    ).group_by(Visit.page).all()

    for r in result:
        print(r)
