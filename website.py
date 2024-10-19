from flask import Flask

website = Flask(__name__)

budgets = {}
spending = {}
credit_scores = {}
savings_goals = {}

@app.route('/')
def home():
    return render_template('index.html')

def setBudget():


def Spending():

def 



