import string
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/play")
def three_boxes():
    return render_template("index.html")

@app.route("/play/<int:num>")
def multiply_boxes(num):
    return render_template("multiply.html", multiply=num)

@app.route("/play/<int:num>/<string:color>")
def multiply_boxes_color(num, color):
    # Have to make a variable to hold the things that we are passing into our parameters of the function. The variable name can be the same as the parameter name i.e. num = num, color = color.
    return render_template("multiplycolor.html", multiply=num,background_color=color)


if __name__ == "__main__":
    app.run(debug = True)