from flask import Flask, render_template
import requests

app = Flask(__name__)

 # This method is convenient when the API returns JSON





@app.route('/blog')
def home():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", dicts=posts)


@app.route('/post/<num>')
def get_blog(num):
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html", title=posts[int(num)]["title"], body=posts[int(num)]["body"] )

if __name__ == "__main__":
    app.run(debug=True)
