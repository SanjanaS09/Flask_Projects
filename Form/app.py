from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

excelfile = "users.xlsx"

if not os.path.exists(excelfile):
    df = pd.DataFrame(columns=['Username', 'Password'])
    df.to_excel(excelfile, index=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    df = pd.read_excel(excelfile)

    new_user = pd.DataFrame({'Username': [username], 'Password': [password]})
    df = pd.concat([df, new_user], ignore_index=True)
    
    df.to_excel(excelfile, index=False)
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        df = pd.read_excel(excelfile)

        user = df[(df['Username'] == username) & (df['Password'] == password)]
        
        if not user.empty:
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
