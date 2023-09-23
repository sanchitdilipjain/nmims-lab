"""Simple Hello World Flask demo app."""

from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():
    """Hello word method."""
    return "Hello Calvine - This is a one step!"


# run the app.
if __name__ == "__main__":
    application.run()
