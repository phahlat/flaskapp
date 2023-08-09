from flask import Flask, make_response, json

application = Flask(__name__)

@application.route("/", methods=["GET", "POST"])
def health():
    return "Hello World!!!"

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port="3000")