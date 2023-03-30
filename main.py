from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:eSec@123@db-hostname/task'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    # Add a new user to the database
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()

    # Query all users from the database
    users = User.query.all()
    return 'Hello World! Users: {}'.format(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
``````````