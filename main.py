from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import bcrypt

# TO DO: finish up setting up the loan html, like, add more functions to it so it's more functional.
# Finish up the HTMLs and the CSS stuff, navigation bars inbetween the logged in routes: credit, loan, budget etc.
# make sure to not delete any of the JS that I set up in the login and register htmls, as well as the log-out functions.

# Any questions regarding templating stuff: 
# https://jinja.palletsprojects.com/en/3.0.x/templates/#tests
# https://www.geeksforgeeks.org/getting-started-with-jinja-template/
# https://www.geeksforgeeks.org/templating-with-jinja2-in-flask/
# {{ }} for expressions.
# {# #} for comments (even multiline) inside the template.
# {% %} for jinja statements (like loops, etc.)
# I encourage you guys to learn templating as it's a great skill! 

# If you want to look into the database, download SQLite, great program to prototype websites that use databases
# https://www.sqlite.org/index.html

# If you guys just want to test out things inside some of the menus you can either load up the HTML by itself without hosting
# or access the account listed below:
# login:    alex
# password: alex
# You might notice that the passwords look all weird in the SQLite file, that's because of bcrypt.


app = Flask(__name__)

app.secret_key = "123"

# connect to the sqlite file
def db_connect():
    db = sqlite3.connect("expenses.sqlite")
    db.row_factory = sqlite3.Row
    return db

#-----------------ROUTES DONE
# TODO: FINISH the htmls and whatever

@app.route("/")
def home():
    return render_template("index.html")


#logout the user as soon as its called by the button
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# This function is done. TO-DO: Finish the HTML.
@app.route('/register', methods=["GET", "POST"])  
def register():
    listoferrors = []
    success = False

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode("utf-8") 
        confirmpwd = request.form['password2'].encode("utf-8")
        # start up the databse
        conn = db_connect()
        cur = conn.cursor()

        # check if the passwords match 
        if password != confirmpwd:
            error = "Passwords do not match"
            listoferrors.append(error)
        
        #3 check if the username is taken
        checkusr = cur.execute('SELECT username FROM people WHERE username = ?', (username,)).fetchone()
        if(checkusr):
            error = "That username is already taken! Pick another one."
            listoferrors.append(error)
        
        # this will help us list all of the previous errors and render them in the page
        if listoferrors:
            return redirect(url_for('register', errors=listoferrors))
        # encrypt passwrod
        hashedpwd = bcrypt.hashpw(password, bcrypt.gensalt())

        # start a connection with the database and send the information there
        cur.execute('INSERT INTO people (username, password, budget, credit, loans) VALUES (?, ?, ?, ?, ?)', 
                    (username, hashedpwd, 1000, 0, 0))
        
        conn.commit()
        conn.close()
        success = True
        
        return render_template('register.html', success=success)
    errors = request.args.getlist('errors')
    return render_template('register.html', errors=errors)


# TO DO:
# finish decorating the page
# add more functions to the page like taking out a loan or whatever
@app.route('/loans')
def loans():

    # IF THE user is not logged in, we send them back to the login page.
    if not session.get("user"):
        error = "User not logged in"
        return redirect(url_for('login', errors=error))
    # catch the users cookie session
    username = session['user']
    
    # connect to the database and retrieve information
    conn = db_connect()
    cur = conn.cursor()

    # call the database and pull out the information
    cur.execute('SELECT * FROM people WHERE username = ?', (username,))
    people = cur.fetchone()
    conn.close()
    
    return render_template('loans.html', user=people)





# TO DO: function is done, figure out a way to catch information
# into other routes just like a session in js 
# https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/
@app.route('/login', methods=['GET', 'POST'])
def login():
    listoferrors = []
    success = False
    
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password'].encode("utf-8")

        #3 start a session so it gets remembered in the other routes
        session['user'] = request.form.get('user')

        # Start up the database
        conn = db_connect()
        cur = conn.cursor()
        user_data = cur.execute('SELECT username, password FROM people WHERE username = ?', (username,)).fetchone()

        if not user_data:
            error = "That username does not exist!"
            listoferrors.append(error)
            return redirect(url_for('login', errors=listoferrors))
        
        db_username, db_password = user_data


        # just to make sure the password is in bytes
        if isinstance(db_password, str):
            db_password = db_password.encode("utf-8")


        # compare the password with the hashed one in the db
        if not bcrypt.checkpw(password, db_password):
            error = "That password does not match!"
            listoferrors.append(error)
            return redirect(url_for('login', errors=listoferrors))

        success = True
        # login successful redirect to budget
        return render_template('login.html', user=db_username, success=success)

    errors = request.args.getlist('errors')
    return render_template('login.html', errors=errors)


# TO DO: check if the user is logged-in
# finish decorating the page
@app.route('/budget/')
def budget():
    # IF THE user is not logged in, we send them back to the login page.
    if not session.get("user"):
        error = "User not logged in"
        return redirect(url_for('login', errors=error))
    # catch the users cookie session
    username = session['user']
    
    # connect to the database and retrieve information
    conn = db_connect()
    cur = conn.cursor()

    # call the database and pull out the information
    cur.execute('SELECT * FROM people WHERE username = ?', (username,))
    people = cur.fetchone()
    conn.close()
    
    return render_template('budget.html', user=people)

# TO DO: check if the user is logged-in
# finish decorating the page
@app.route('/credit')
def credit():

    # IF THE user is not logged in, we send them back to the login page.
    if not session.get("user"):
        error = "User not logged in"
        return redirect(url_for('login', errors=error))
    # catch the users cookie session
    username = session['user']
    
    # connect to the database and retrieve information
    conn = db_connect()
    cur = conn.cursor()

    # call the database and pull out the information
    cur.execute('SELECT * FROM people WHERE username = ?', (username,))
    people = cur.fetchone()
    conn.close()
    
    return render_template('credit.html', user=people)

if __name__ == '__main__':
    app.run(debug=True)