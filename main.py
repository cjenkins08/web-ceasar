from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True




form = """

<!DOCTYPE html>
<html>
    <head>
        <style>
        form{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto; 
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px; 
        }
        textarea {
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }
    </style>
     </head>
    <body>
   <!-- @todo set a form action to a route that takes the input and rotates the characters -->
   <form action="encrypt", method ='POST'>
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
    return form


@app.route("/encrypt", methods =["POST"])
def encrypt(text, rot):
    r_info = request.form['rot']
    new_msg = request.form['text']
    new_string = rotate_string (new_msg, r_info)
    formated_string = new_string

    return form.format(formated_string)

app.run()




