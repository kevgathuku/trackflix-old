from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return "Hello World!"

@app.route('/users/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Welcome %s' % username


if __name__ == "__main__":
    app.run(debug=True)
