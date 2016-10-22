from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property

from app import db


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    overview = db.Column(db.Text)
    homepage = db.Column(db.String(250))
    status = db.Column(db.String(50))
    poster_path = db.Column(db.String(100))
    backdrop_path = db.Column(db.String(100))
    _first_air_date = db.Column(db.Date)
    origin_country = db.Column(db.String(10))

    seasons = db.relationship('Season', backref='show', lazy='dynamic')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @hybrid_property
    def first_air_date(self):
        """Returns the computed date object"""

        return self._first_air_date

    @first_air_date.setter
    def _set_first_air_date(self, date_string):
        """Convert a date string to a Python date object"""

        self._first_air_date = datetime.strptime(
            date_string, '%Y-%m-%d').date()

    def __repr__(self):
        return '<Show: %r>' % self.name


class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), index=True)
    overview = db.Column(db.Text)
    number = db.Column(db.SmallInteger)
    poster_path = db.Column(db.String(100))
    air_date = db.Column(db.Date)
    episode_count = db.Column(db.SmallInteger)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))

    episodes = db.relationship('Episode', backref='season', lazy='dynamic')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Season: %r>' % self.number


class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), index=True)
    overview = db.Column(db.Text)
    episode_number = db.Column(db.SmallInteger)
    still_path = db.Column(db.String(100))
    air_date = db.Column(db.Date)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Episode: %r>' % self.name
