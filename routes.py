from flask import Flask, render_template, request
from models import db, User
from forms import SignupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qmdcdbzokzopss:be0cea0dde44a66115cf3f0acfb8108534e979053172f4f0682432c4550dabe7@ec2-54-204-41-109.compute-1.amazonaws.com:5432/d36isgf1valhqu'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
      return 'Success!'

  elif request.method == "GET":
    return render_template('signup.html', form=form)

if __name__ == "__main__":
  app.run(debug=True)
