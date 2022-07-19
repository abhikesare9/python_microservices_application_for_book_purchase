from pickle import FALSE
from flask import Flask
from routes import book_blueprint
from models import db,Book,init_app
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'N7g1bC_0jeuPI_7LqtXRDA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = FALSE

app.register_blueprint(book_blueprint)
init_app(app)

migreate = Migrate(app,db)

if __name__ == "main":
    app.run(host='0.0.0.0',port='5002')