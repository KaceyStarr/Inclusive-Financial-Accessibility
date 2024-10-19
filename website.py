from flask import Flask

website = Flask(__name__)

budgets = {}
spending = {}

@app.route('/')
def home():
    return render_template('.html')

