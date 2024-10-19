@app.route('/budget/')
def budget():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM people')
    people = cur.fetchall()
    conn.close()
    
    return render_template('budget.html', people=people)