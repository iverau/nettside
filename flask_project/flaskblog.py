from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': "Iver",
        'title': "Post 1",
        'content': "First post content",
        'date_posted': 'April 20, 2018'
    },
    {
        'author': "Knut",
        'title': "Post 2",
        'content': "Second post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post content",
        'date_posted': 'April 20, 2018'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts,title="Test")

@app.route("/about")
def about():
    return render_template("about.html", posts=posts,title="Test2")