# import flask
from flask import Flask

# define webpage
app = Flask(__name__)

# define home page
@app.route('/')

# content in home page
def helloPets():
    return '<h2><b> Helloo Sally, Suria and Anna</h2></b>'

# Execution Procedure
# In Command Prompt : - set FLASK_APP=<file_name>
#                     - set FLASK_ENV=development
#                     - flask run
# Read the output message. Run the HTTP link.

