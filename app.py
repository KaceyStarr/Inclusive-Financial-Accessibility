from flask import Flask, render_template, request

app = Flask(__name__)

budgets = {}
spending = {}
credit_scores = {}
savings_goals = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/budget', methods=['POST'])
def budget():
    user = request.form['user']

@app.route('/savings', methods=['POST'])
def saving():
    user = request.form['user']

@app.route('/credit', methods=['POST'])
def credit():
    usesr = request.form['user']