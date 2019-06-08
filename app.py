from flask import Flask, render_template, redirect, url_for
import datetime
currentDT = datetime.datetime.now()

card = {"img_url": "Image-Here.png",
        "is_new": True,
        "is_featured": True,
        "is_super": True,
        "title": "Giveaways",
        "text": "Something here..",
        "uploaded": currentDT.strftime("%Y-%m-%d %H:%M:%S"),
        "views": "Can't be counted yet."}

cards = [card, card, card, card, card, card, card]


app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/home")
def home():
    return render_template("home.html", cards=cards)


@app.route("/intro")
def intro():
    return render_template("intro.html")


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
