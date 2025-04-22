from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    converted = None
    amount = 0
    from_currency = 'USD'
    to_currency = 'INR'
    
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
        response = requests.get(url)
        data = response.json()
        converted = data['rates'].get(to_currency)

    currencies = ['USD', 'EUR', 'INR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY']
    return render_template('index.html', converted=converted, amount=amount, from_currency=from_currency, to_currency=to_currency, currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
