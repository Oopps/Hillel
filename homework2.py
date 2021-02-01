from flask import Flask, request
from faker import Faker
import pandas as pd
import requests

fake = Faker()
app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    req_data = open('requirements.txt', 'r')
    return req_data.read()


@app.route('/generate-users/')
def generate():
    users = {}
    user_count = request.args.get('user_count', 100)
    for i in range(int(user_count)):
        users[fake.name()] = fake.ascii_email()
    return str(users)


@app.route('/mean/')
def mean():
    data = pd.read_csv('hw.csv')
    height = data[' "Height(Inches)"'].mean() * 2.54
    weight = data[' "Weight(Pounds)"'].mean() * 0.453592
    return 'Height: ' + str(height) + ', Weight: ' + str(weight)


@app.route('/space/')
def astro_qty():
    astro = requests.get('http://api.open-notify.org/astros.json')
    qty = astro.json()['number']
    return str(qty)
