from flask import Flask
from model import Customer
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
 
db = SQLAlchemy(app)


@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run()
