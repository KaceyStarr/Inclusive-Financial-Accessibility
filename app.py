from flask import Flask, render_template, request

app = Flask(__name__)

budgets = {}
spending = {}
credit_scores = {}
savings_goals = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_budget', methods=['POST'])
def set_budget():
    user = request.form['user']


@app.route('/add_transaction' methods=['POST'])
def add_transaction():
    user = request.form['user']



