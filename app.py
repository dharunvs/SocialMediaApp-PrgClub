from flask import Flask, render_template, request
from dbfunctions import *


app = Flask(
        __name__,
        template_folder="./client/templates",
        static_folder="./client/static"
    )



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        delete_all()
        return render_template('index.html')
    else:
        name = request.form['name']
        message = request.form['message']
        add_post(name, message)
        post = get_info()
        return render_template(
            'index.html',
            info=post)

    
if __name__ == "__main__":
    app.run(debug=True)