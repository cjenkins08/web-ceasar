from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True




form = """

<!DOCTYPE html>
<html>
    <head>
        <style>
        
        </style>
     </head>
    <body>
   <!-- @todo set a form action to a route that takes the input and rotates the characters -->
   <form action="/encrypt", method ='POST'>
        <label>
            Rotating Number
            <input name="rot" value="0" type="text" />
        </label>
        
        <br>
        
        <label>
            <textarea name="message"> {0} </textarea>
        </label>
        
        <input type="submit"/>
     </body>
    </html>
"""


@app.route("/")
def index():
    return form.format('')


@app.route("/encrypt", methods =["POST"])
def encrypt():
    r_info = request.form['rot']
    new_msg = request.form['message']
    new_string = rotate_string(new_msg, int(r_info))
    

    return form.format(new_string)

app.run()




