from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect('sum_form')

@app.route('/sum_form', methods=['GET', 'POST'])
def summing():
    if request.method == 'GET':
        return render_template('sum.html')
    elif request.method == 'POST':
        username = request.form['username']
        a = int(request.form['a'])
        b = int(request.form['b'])

        return render_template('result.html', sum=a+b, username=username)

if __name__ == "__main__":
	app.run(debug=True)