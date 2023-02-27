from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test_dev")
def test_dev():
    return "Deployment success! OMG! "


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)