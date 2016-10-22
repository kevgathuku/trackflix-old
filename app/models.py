from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB

from app import db


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(100), index=True)
    overview = db.Column(db.Text)
    # Other fields accessed from API response
    tmdb_data = db.Column(JSONB)

    seasons = db.relationship('Season', backref='show', lazy='dynamic')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Show: %r>' % self.name


class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(250), index=True)
    overview = db.Column(db.Text)
    season_number = db.Column(db.SmallInteger)

    tmdb_data = db.Column(JSONB)

    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))
    episodes = db.relationship('Episode', backref='season', lazy='dynamic')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<%r>' % self.name


class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(250), index=True)
    overview = db.Column(db.Text)
    episode_number = db.Column(db.SmallInteger)

    tmdb_data = db.Column(JSONB)

    season_id = db.Column(db.Integer, db.ForeignKey('season.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Episode: %r>' % self.name
