from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here

    getAll = requests.get('')

    return render_template('index.html', data=getAll.json())


if __name__ == '__main__':
    app.run()
