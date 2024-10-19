from flask import Flask, render_template, request
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("budgetbuddy"),
    autoescape=select_autoescape()
) 

app = Flask(__name__)

budgets = {}
spending = {}
credit_scores = {}
savings_goals = {}

@app.route('/')
def home():
    return render_template('budget.html', budget = 10)

# @app.route('/budget', methods=['POST'])
# def budget():
#     user = request.form['user']

# @app.route('/savings', methods=['POST'])
# def saving():
#     user = request.form['user']

# @app.route('/credit', methods=['POST'])
# def credit():
#     user = request.form['user']
#     credit_scores = int(request.form['credit_score'])
#     credit_scores[user] = credit_scores

if __name__ == '__main__':
    app.run(debug=True)