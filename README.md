## Getting Started

Clone this repository to your local machine.

(Optional) Create and activate a Python virtual environment based on your operating system.  
You can also visit [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx) if working with APIs that require keys.

Install required dependencies using pip:

```
pip install flask requests
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





