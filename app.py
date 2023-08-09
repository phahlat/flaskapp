from flask import Flask, make_response, json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def health():
    return make_response(json.dumps({"status": "OK"}))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="3000")