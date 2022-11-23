from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import UserSchema
from models import UserModel
from db import db
from flask_jwt_extended import jwt_required,create_access_token
from passlib.hash import pbkdf2_sha1

blp = Blueprint("User","user","Operations on users")

@blp.route("/")
class Home(MethodView):
    def get(self):
        return {"message":"Home Page"}
    

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self,user_data):
        user = UserModel(name=user_data["name"],
                         email=user_data["email"],
                         password=pbkdf2_sha1.hash(user_data["password"]))
        at = create_access_token(identity=user.id)
        db.session.add(user)
        db.session.commit()
        return {"message":"user registered successfully","access_token":at}
    
@blp.route("/users")
class GetUsers(MethodView):
    @blp.response(200,UserSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return users