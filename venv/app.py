from flask import Flask
from resources.user import blp as UserBlueprint
from flask_smorest import Api
from db import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["API_TITLE"]="ANDROID API"
app.config["API_VERSION"] ="v1"
app.config["OPENAPI_VERSION"] ="3.0.3"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SCQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"]= "secretkey"

jwt = JWTManager(app)

db.init_app(app)
api = Api(app)
api.register_blueprint(UserBlueprint)

@app.before_first_request
def create_tables():
    db.create_all()
    
def new_code():
    pass


