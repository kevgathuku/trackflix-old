from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property

from app import db


show_people = db.Table(
    'show_people',
    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
    db.Column('show_id', db.Integer, db.ForeignKey('show.id')),
    db.Column('role', db.String(100))
)

show_genres = db.Table(
    'show_genres',
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id')),
    db.Column('show_id', db.Integer, db.ForeignKey('show.id'))
)


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
    popularity = db.Column(db.Float)

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


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    biography = db.Column(db.Text)
    birthday = db.Column(db.Date)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Person: %r>' % self.name


class PersonExternalId(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(20))
    identifier = db.Column(db.String(150), unique=True)

    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ShowExternalId(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(20))
    identifier = db.Column(db.String(150), unique=True)

    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # Genres have a TVDB id
    identifier = db.Column(db.String(150))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Genre: %r>' % self.name


class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.SmallInteger)
    poster_path = db.Column(db.String(100))
    air_date = db.Column(db.Date)
    episode_count = db.Column(db.SmallInteger)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Season: %r>' % self.number
