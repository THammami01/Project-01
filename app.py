from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/featured")
def featured():
    return render_template("featured.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(403)
def error403(a):
    return render_template("403.html", a=a)


@app.errorhandler(404)
def error404(a):
    return render_template("404.html", a=a)


@app.errorhandler(500)
def error500(a):
    return render_template("500.html", a=a)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3303, debug=True)
