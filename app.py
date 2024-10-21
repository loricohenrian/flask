from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# Set a SECRET_KEY for forms and CSRF protection
app.config['SECRET_KEY'] = '30a9c161f25a46f1d97998c10bd0b1f8'

# Sample posts to render on the homepage
posts = [
    {
        'author': 'Henrian Lorico',
        'title': 'Blog Post 1',
        'content': 'First content',
        'date_posted': 'April 20, 4025'
    },
    {
        'author': 'Panot Lorico',
        'title': 'Blog Post 2',
        'content': 'Second content',
        'date_posted': 'April 3, 4025'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.passsword.data == "password":
            flash("You have been logged in!", 'success')
            return redirect(url_for('homE'))
        else:
            flash('Login Unsuccesful. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)
