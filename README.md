## Getting Started

Clone this repository to your local machine.

(Optional) Create and activate a Python virtual environment based on your operating system.  
You can also visit [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx) if working with APIs that require keys.

Install required dependencies using pip:

```
pip install flask requests numpy
```

Run your server:

```
python app.py
```

---

## API Overview

- **GET /**  
  Returns a plain "Hello World!" message.  
  Used to verify the server is running.

- **POST /echo**  
  Accepts a JSON payload in the request body and returns it back in the response.  
  Demonstrates how user input is received and returned.

- **GET /pokemon/<name>**  
  Proxies a request to the public [PokeAPI](https://pokeapi.co/) and returns real-time Pokémon data.  
  Shows how a Flask app can interact with an external API to serve live data.

- **POST /multiply**
  Accepts two or three matrices (A, B, and optionally C) in JSON format and returns the result of matrix multiplication.
  Demonstrates how server-side computation is done using NumPy.

- **POST /power**  
  Accepts a JSON payload with `base` and `exponent`, and returns the result of raising the base to the exponent using exponentiation by squaring.  
  Efficient for large powers and supports negative exponents.  

- **POST /matrix_power**
  This route accepts a square matrix and an integer exponent, and efficiently computes the matrix raised to that power using exponentiation by squaring. It also handles negative exponents (via matrix inversion).

- **POST /matrix_power_plain**
  Raises a square matrix (with integer values) to a given exponent using pure Python, without NumPy.


