from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
def student():
    f = open("whitelist.txt", "r")
    return render_template('student.html', content=[f.read()])


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
