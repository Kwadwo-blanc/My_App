from flask import Flask, render_template,request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(_name_)
app.config["SECRET KEY"] = "your_secret_key_here"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def _init_(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(int(user_id))

@app.route("/")
def index():
    return render_template("index.html")


if _name_ == "_main_":
    app.run(debug=True)
