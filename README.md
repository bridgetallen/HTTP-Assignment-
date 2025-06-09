Preliminary steps: 

1. Make a new repository on the github browser, in this case, clone this repository

In Ubuntu:

2.  Go to your main project directory (e.g. suli folder), then create a new module for the project (e.g. flask-http-assignment). Make sure to stay in this directory at all times during the project.

3. Create and/or activate virtual environment.

4. pip install flask and requests. 

5. create app.py.

6. in the vim, Built a Flask Server with Three Endpoints (see app.py for code).

GET /
Returns a plain "Hello World!" message.

POST /echo
Accepts JSON in the request body and returns it back in the response (an echo server).

GET /pokemon/<name>
Acts as a proxy to the PokeAPI, returning real-time Pokémon data for any name passed in the URL (e.g., /pokemon/eevee).

7. esc, :wq, enter to leave the vim.

8. run your server with python app.py.

9. for the first end point: open http link (given in the output for python app.py) and see hello world.

10. for the second end point: open a new ubuntu tab and use the curl command and http link plus "/echo \" to enter the content type and a message to see the echo reflected in the output.

11. for the third end point: manually type in any pokemon to the end of the http link to see the output example: add "/pikachu".

12. initilize git, add your files, commit, specify branch, add origin (URL from browser), push (anytime you need to make changes to the code in vim, you must stage changes, commit them, and push them).

13. Check github to ensure your changes are saved.
