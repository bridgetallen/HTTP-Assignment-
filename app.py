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

# 🟡 Proxy endpoint — PokeAPI proxy for any Pokémon
@app.route("/pokemon/<name>", methods=["GET"])
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Pokémon not found"}), response.status_code


if __name__ == "__main__":
    app.run(debug=True)

