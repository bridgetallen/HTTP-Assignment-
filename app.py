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

@app.route("/multiply", methods=["POST"])
def multiply_matrices():
    data = request.get_json()

    try:
        A = data["A"]
        B = data["B"]
        C = data.get("C")  # optional third matrix

        import numpy as np
        result = np.matmul(A, B)
        if C:
            result = np.matmul(result, C)

        return jsonify({"result": result.tolist()}), 200  # ✅ convert ndarray to list

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/power", methods=["POST"])
def power():
    data = request.get_json()
    base = data.get("base")
    exponent = data.get("exponent")

    if not isinstance(base, (int, float)) or not isinstance(exponent, int):
        return jsonify({"error": "Base must be a number, exponent must be an integer."}), 400

    result = 1
    b = base
    e = exponent

    if e < 0:
        b = 1 / b
        e = -e

    while e > 0:
        if e % 2 == 1:
            result *= b
        b *= b
        e //= 2

    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(debug=True)

