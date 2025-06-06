Preliminary steps: 

1. Make a new repository in github 

In Ubuntu:

1.  Create a new module for the project and put it in  the suli folder (make sure you're in this directory at all times)

2. Activate virtual environment

3. Install flask 

4. cd into the file that holds the flask app 

5. create app.py

6. in the vim, Built a Flask Server with Three Endpoints

GET /
Returns a plain "Hello World!" message

POST /echo
Accepts JSON in the request body and returns it back in the response (an echo server)

GET /pokemon/<name>
Acts as a proxy to the PokeAPI, returning real-time Pokémon data for any name passed in the URL (e.g., /pokemon/eevee)

7. esc, :wq, enter

8. run app.py

9. for the first end point: open http link and see hello world

10. for the second end point: open a new ubuntu tab and use the curl command to see the echo 

11. for the third end point: add any pokemon to the end of the link to see the output example: /pikachu

12. initilize git, add your files, commit, add origin (URL from browser), push 
