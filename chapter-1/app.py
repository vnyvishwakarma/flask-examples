
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>The HTML5 Vinay Kr. Vishwakarma</title>
        <meta name="description" content="The HTML5 Vinay">
    </head>
    <body>
        <h1> This is home page rendered from flask </h1>
    </body>
    </html>
    '''
@app.route("/about")
def about():
    return '<h2> This is about page </h2>'

if __name__ == '__main__':
    app.run(debug=True)