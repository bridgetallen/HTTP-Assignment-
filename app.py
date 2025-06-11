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
@app.route("/matrix_power", methods=["POST"])
def matrix_power():
    data = request.get_json()
    matrix = data.get("matrix")
    exponent = data.get("exponent")

    if not isinstance(matrix, list) or not isinstance(exponent, int):
        return jsonify({"error": "Matrix must be a list of lists and exponent must be an integer."}), 400

    try:
        import numpy as np
        A = np.array(matrix)

        if A.shape[0] != A.shape[1]:
            return jsonify({"error": "Matrix must be square (same number of rows and columns)."}), 400

        def matrix_exp(A, exp):
            result = np.identity(A.shape[0])
            if exp < 0:
                A = np.linalg.inv(A)
                exp = -exp
            while exp > 0:
                if exp % 2 == 1:
                    result = np.matmul(result, A)
                A = np.matmul(A, A)
                exp //= 2
            return result

        powered = matrix_exp(A, exponent)
        return jsonify({"result": powered.tolist()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
#  Plain matrix multiplication
def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError("Matrix dimensions do not allow multiplication")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

#  Exponentiation by squaring for square matrices
def matrix_power(matrix, exponent):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")

    # Identity matrix
    size = len(matrix)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    while exponent > 0:
        if exponent % 2 == 1:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        exponent //= 2

    return result

#  New Flask route
@app.route("/matrix_power_plain", methods=["POST"])
def matrix_power_plain():
    data = request.get_json()
    try:
        matrix = data["matrix"]
        exponent = int(data["exponent"])
        result = matrix_power(matrix, exponent)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)

