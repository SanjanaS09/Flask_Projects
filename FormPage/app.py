from flask import Flask, render_template
from forms import SignUpForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

@app.route('/')
def home():
   return 'Hello World'

@app.route('/about')
def about():
   return 'This is about page'

@app.route('/blog')
def blog():
   posts = [{'title': 'Technology in 2019', 'author': 'Sanjana'}]
   posts = [{'title': 'ABCD', 'author': 'Sneha'}]
   return render_template('blog.html', author = 'Shreya', sunny = True, posts = posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
   return f'This is blog post' + blog_id

@app.route('/signup', methods =['GET', 'POST'])
def signup():
   form = SignUpForm()
   return render_template('signup.html', form=form)

@app.route('/sucsess')
def success():
   return "sign up successsfull"

if __name__ =='__main__':
   app.run()

