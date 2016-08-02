from app import app


@app.route('/')
@app.route('/home')
def hello():
    return "Hello World!"

@app.route('/users/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Welcome %s' % username
