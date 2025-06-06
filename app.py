from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World!"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

@app.route("/pokemon/<name>", methods=["GET"])
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=True)

