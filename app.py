from flask import Flask, render_template, request

website = Flask(__name__)

budgets = {}
spending = {}
credit_scores = {}
savings_goals = {}

@app.route('/')
def home():
    return render_template('index.html')

def set_budget():
    budgets
def add_transaction():

def saving_goal():



