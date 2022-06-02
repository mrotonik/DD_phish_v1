import phishing_detection
from flask import Flask
from flask import (
    render_template, request
)
app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def hello():
	if request.method == 'POST':
		try:
			username = request.form.get('DDK')
			return render_template("getInput.html",items=phishing_detection.getResult(username))
		except:
			pass
	return  render_template("getInput.html")
if __name__ == '__main__':
    app.run(debug=True)
