from flask import Flask, render_template, request
from prime_numbers import find_primes
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/primes', methods=['POST'])
def primes():
    num = int(request.form['num'])
    result = find_primes(num)
    return render_template('primes.html', result=result)

@app.route('/back_home')
def back_home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)