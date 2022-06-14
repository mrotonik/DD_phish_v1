import os

import phishing_detection
from flask import Flask, current_app
from flask import (
    render_template, request
)

from flask import send_from_directory
from os import path
app = Flask(__name__)




@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'POST':
        try:
            username = request.form.get('DDK')
            return render_template("getInput.html",items=phishing_detection.getResult(username),disabled='enabled')
        except:
            pass
    return  render_template("getInput.html",disabled='disabled')
@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    directory = path.join(app.root_path, app.config['FOLDER_WIT_FILE'])
    return send_from_directory(directory=directory, filename=filename)
if __name__ == '__main__':
    app.run(debug=True)
