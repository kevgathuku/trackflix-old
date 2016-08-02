from datetime import datetime

from app import db


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    overview = db.Column(db.Text)
    homepage = db.Column(db.String(250))
    status = db.Column(db.String(50))
    poster_path = db.Column(db.String(100))
    backdrop_path = db.Column(db.String(100))
    first_air_date = db.Column(db.Date)
    origin_country = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # What to refer the model as in the corresponding Model
    creators = db.relationship(
        'Person', backref='created_shows', lazy='dynamic')
    external_ids = db.relationship(
        'ExternalId', backref='show', lazy='dynamic')


class ExternalId(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(20))
    identifier = db.Column(db.String(150), unique=True)

    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    biography = db.Column(db.Date)
    birthday = db.Column(db.Text)

    shows = db.Column(db.Integer, db.ForeignKey('show.id'))
