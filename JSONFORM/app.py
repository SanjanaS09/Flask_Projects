from flask import Flask, redirect, render_template, url_for, request, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

users_db = {
    'user1': {"name": "Anna", "email": "Anna@abc.com", "password": "12345678"},
    'user2': {"name": "John", "email": "John@abc.com", "password": "987654321"},
    'user3': {"name": "Peter", "email": "Peter@abc.com", "password": "15975312"}
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users_db.get(username)
        if user:
            if user['password'] == password:
                return redirect(url_for('home'))
            else:
                message = "Invalid credentials, password does not match."
        else:
            message = "Invalid credentials, user not found."
    
    return render_template('login.html', message=message)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if username in users_db:
            message = "Signup failed, user already exists"
        else:
            users_db[username] = {
                'name': username,
                'email': email,
                'password': password
            }
            return redirect(url_for('login'))

    return render_template('signin.html', message=message)

if __name__ == '__main__':
    app.run()
