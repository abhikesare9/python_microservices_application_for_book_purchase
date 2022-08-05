
from flask import Flask
from routes import user_blueprint
from flask_migrate import Migrate
import models
from flask_login import LoginManager
from flask import g
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CJEnExvPBocmKR5O0cMJsw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database/user.db'
models.init_app(app)
app.register_blueprint(user_blueprint)
login_manager = LoginManager(app)
migrate = Migrate(app,models.db)

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id).first()


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic','',1)
        user = models.User.query.filter_by(api_key=api_key).first()
        if user:
            return user
    return None

class CustomSessionInterface(SecureCookieSessionInterface):

    def save_session(self, *args,**kwargs):
        if g.get('login_via_loader'):
            return
        return super(CustomSessionInterface,self).save_session(*args,**kwargs)
if __name__ == "main":
    app.run(port=5001,debug=True)