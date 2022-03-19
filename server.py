from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return app.make_response("OK")


if __name__ == "__main__":
    app.run()
