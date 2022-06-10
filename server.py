import string
from flask import Flask, render_template
app = Flask(__name__)

# If you stack app routes on top of each other, all of them will take the function below.
@app.route("/play")
@app.route("/play/<int:num>")
@app.route("/play/<int:num>/<string:color>")
# set defaults so that the static one will have these properties when you do not pass anything into the function, then the more dynamic ones will override these defaults.
def multiply_boxes_color(num = 3, color = "teal"):
    # Have to make a variable to hold the things that we are passing into our parameters of the function. The variable name can be the same as the parameter name i.e. num = num, color = color.
    return render_template("multiplycolor.html", multiply=num,background_color=color)


if __name__ == "__main__":
    app.run(debug = True)