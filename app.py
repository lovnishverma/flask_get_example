from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sum', methods=['GET', 'POST'])
def sum():
    # num1 = int(request.args.get('a'))
    num1 = int(request.form.get('a'))
    num2 = int(request.form.get('b'))
    result = num1 + num2
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
