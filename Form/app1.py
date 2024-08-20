from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

csvfile = "users.csv"

if not os.path.exists(csvfile):
    df = pd.DataFrame(columns=['Username', 'Password'])
    df.to_csv(csvfile, index=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    df = pd.read_csv(csvfile)

    new_user = pd.DataFrame({'Username': [username], 'Password': [password]})
    df = pd.concat([df, new_user], ignore_index=True)
    
    df.to_csv(csvfile, index=False)
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        df = pd.read_csv(csvfile)

        user = df[(df['Username'] == username) & (df['Password'] == password)]
        
        if not user.empty:
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
