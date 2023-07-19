from flask import Flask, render_template
from flask import request
import requests
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators = [DataRequired()])
    password = PasswordField(label='Password', validators = [DataRequired()])
    submit = SubmitField(label='Log In')



app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", dicts=posts)


@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact')
def get_contact():
    return render_template("contact.html")

@app.route('/contact', methods=["GET", "POST"])
def receiver_data():
    
    if request.method == 'POST':
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
       # if login_form.email.data == "carlos@gmail.com" &  login_form.password.data == '1234':
       #     return render_template('success.html', form=login_form)
       # else:
       #    return render_template('denied.html', form=login_form)
    return render_template('login.html', form=login_form)

#@app.route('/post/<num>')
#def get_post():
#    return render_template("post.html")

#@app.route('/post/<num>')
#def get_blog(num):
  #  posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
 #   return render_template("post.html", title=posts[int(num)]["title"], body=posts[int(num)]["body"] )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
