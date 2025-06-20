from flask import Flask
from app.routes.main import main as main_blueprint
from app.routes.auth import auth as auth_blueprint
from flask_login import LoginManager
from app.models.Db_models import User, session
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.secret_key=os.getenv('SECRET_KEY')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='auth.login'
csrf = CSRFProtect()
csrf.init_app(app)

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
@login_manager.user_loader
def load_user(user_id):
  return session.query(User).get(int(user_id))