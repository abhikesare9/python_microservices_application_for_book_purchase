
from flask import Flask
from routes import order_bluprint
from models import db, init_app
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '7RAS2OWLPTm5r0DfCqCd9w'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/order.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(order_bluprint)

init_app(app)
migrate = Migrate(app,db)

if __name__ == "main":
    app.run(debug=True,port=5003)
