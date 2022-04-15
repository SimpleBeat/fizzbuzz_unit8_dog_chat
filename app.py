from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():

    testPosts = [
        "So great to be here!",
        "I love DogChat!!",
        "Time to go for a quick walk. See ya all soon."
    ]

    return render_template('index.html', posts = testPosts)