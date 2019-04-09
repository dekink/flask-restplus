from flask import Flask, render_template, request, redirect, url_for
from api.swagger import blueprint
import stripe
import os

pub_key = 'pk_test_iOpIzptrQvCVGOuVOTwH870g008eEhq9Ys'
secret_key = os.environ['STRIPE_SECRET_KEY']

stripe.api_key = secret_key

app = Flask(__name__, template_folder='templates')
app.register_blueprint(blueprint)

@app.route('/')
def index():
    return render_template('index.html', pub_key = pub_key)

@app.route('/pay', methods=['POST'])
def pay():
    data = request.form
    customer = stripe.Customer.create(email=data['stripeEmail'], source=data['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=100,
        currency='usd',
        description='The Product'
    )
    return render_template('payments/thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
