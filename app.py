from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.add_template_global(len, name='len')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:admin@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
