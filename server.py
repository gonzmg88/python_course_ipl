from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello IPL!"

if __name__ == "__main__":
    app.run(port=6969, host="0.0.0.0")
