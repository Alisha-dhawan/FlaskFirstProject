from flask import Flask, render_template, request
from models import db, user
from forms import SignupForm
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/demo'
db.init_app(app)
app.secret_key = "development-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
    form = SignupForm()
    if request.method == "POST":
        print("method called")
        if not form.validate_on_submit():
            return render_template('signup.html', form=form)
        else:
            newuser = user(form.first_name.data,form.last_name.data,form.email.data,form.password.data)
            db.session.add(newuser)
            db.session.commit()
            return "success"
    elif request.method=="GET":
        return render_template('signup.html',form=form)

if __name__=="__main__":
    app.run(debug=True)