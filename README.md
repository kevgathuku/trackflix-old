# TrackFlix

A TV Series Tracking Application.  
_The smart way to keep track of the TV series you watch_

### Rationale

Have you ever started watching a TV Series, took a break from it for a while,
then when you finally find some time to get back to it, you find out you completely forgot where you left it off?

This application makes sure you never have to deal with this again.

Simply check off the episodes you have watched, and the next time you go back to
watching your series, you can easily find out where you left off.

## Inspiration

- [Twee](https://twee-app.com/) - A mobile app for tracking TV series on your phone.
- [Movieo](https://movieo.me) - A mobile-friendly website for tracking movies both on mobile and desktop.

## Installation

### Dependencies

You need to install the following to get started:

1. [Python 2](https://python.org)
2. [PostgreSQL](http://www.postgresql.org/download/macosx/)
3. [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/) (Optional but highly recommended)

## Local Setup

- Clone the repo locally and navigate to the newly created folder

```sh
git clone https://github.com/kevgathuku/trackflix
cd trackflix
```

Create a virtual environment to avoid polluting your global pip dependencies

```sh
mkvirtualenv trackflix
```

 - Install the app dependencies

```sh
pip install -r requirements.txt
```

 - Create a `.env` file where you will store your environment variables

 ```sh
 cp .env.example .env
 ```
 Make sure to enter a valid [`DATABASE_URL`](http://flask-sqlalchemy.pocoo.org/2.1/config/#connection-uri-format)

Run the database migrations to create the required tables in the DB

```sh
$ python manage.py db upgrade
```

To run the application:

```sh
$ python manage.py runserver
```

### Required Environment Variables

- `DATABASE_URL` - Database Configuration
- `TMDB_API_KEY` - Required for communicating with [The Movie DB](https://www.themoviedb.org/)'s API

Get your API key [here](https://www.themoviedb.org/account).

Now visit `http://localhost:5000` to view the application on your preferred web browser.

## License
Copyright (c) 2016 __Kevin Ndung'u__  
Licensed under the [MIT license](http://mit-license.org/)
