from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Security key for database access
SECURITY_KEY = "4477"
MAX_ATTEMPTS = 3

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    E_Mail = db.Column(db.String(200), nullable=False)
    Passwords = db.Column(db.String(400), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User(Sno={self.Sno}, E_Mail='{self.E_Mail}')"

# Middleware to handle database security
@app.route('/view-database', methods=['GET', 'POST'])
def view_database():
    if 'attempts' not in session:
        session['attempts'] = 0  # Initialize attempts counter

    if request.method == 'POST':
        s_password = request.form['s_password']
        if s_password == SECURITY_KEY:
            session.pop('attempts', None)  # Reset attempts on success
            show_data = User.query.all()
            return render_template('database.html', show_data=show_data)
        else:
            session['attempts'] += 1
            if session['attempts'] >= MAX_ATTEMPTS:
                flash("Database not accessible at this time. Please try later.")
                session.pop('attempts', None)  # Reset attempts
                return redirect('/')
            flash(f"Incorrect key! {MAX_ATTEMPTS - session['attempts']} attempts remaining.")

    return render_template('key_prompt.html')

# Remaining routes (e.g., home, update, delete)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User(E_Mail=email, Passwords=password)
        db.session.add(user)
        db.session.commit()
    return render_template('index.html')

@app.route('/delete/<int:Sno>')
def delete(Sno):
    user = User.query.filter_by(Sno=Sno).first()
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect('/view-database')

@app.route('/update/<int:Sno>', methods=['GET', 'POST'])
def update(Sno):
    user = User.query.filter_by(Sno=Sno).first()
    if not user:
        return "User not found", 404
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user.E_Mail = email
        user.Passwords = password
        db.session.commit()
        return redirect('/view-database')
    return render_template('update.html', show_data=user)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database is created before starting the app
    app.run(debug=True, port=8800)