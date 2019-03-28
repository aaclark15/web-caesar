from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          form {{
              background-color: #eee;
              padding: 20px;
              margin: 0 auto;
              width: 540px;
              font: 16px sans-serif;
              border-radius: 10px;
          }}
          textarea {{
              margin: 10px;
              width: 540px;
              height: 120px;
          }}
        </style>
      </head>    
      <body>
        <form method = "POST">

        <label for="rot">Rotate by: </label> 
        <input type="text" name="rot" id="rot" value="0" />
        <br><br>      

        <label>Message Here: 
            <textarea name="text">{0}</textarea>
        </label>
        <br>

        <input type="submit" />

      </body>  
    </html>
"""

@app.route("/")
def index(): 
    return form.format('')

@app.route("/", methods=["POST"])
def encrypt():
    rotate = request.form['rot']
    message = request.form['text']

    rotate = int(rotate)

    new_msg = rotate_string(message, rotate)

    return form.format(new_msg)


app.run()

