from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🟢 GET endpoint — Hello World
@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World!"

# 🔵 POST endpoint — Echo
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

@app.route("/pokemon/<name>", methods=["GET"])
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
# 🟡 Proxy endpoint — PokeAPI proxy
@app.route("/pokemon", methods=["GET"])
def get_pikachu():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    response = requests.get(url)
    return jsonify(response.json()), response.status_code
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)

