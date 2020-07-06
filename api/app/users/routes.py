from flask import request
from flask_jwt_extended import create_access_token
from app import db
from app.users import users_bp
from app.users.models import User
from app.users.schema import UserSchema
from app.utils.responses import response_with
from app.utils import responses as resp


@users_bp.route('/register', methods=['POST'])
def create_user():
    """
    用户注册接口
    ---
    parameters:
        - in: body
          name: body
          schema:
            required:
                - username
                - password
            properties:
                username:
                    type: string
                    description: 用户名
                    default: ""
                password:
                    type: string
                    description: 用户密码
                    default: ""
    responses:
        201:
            description: 注册成功
            schema:
                properties:
                    code:
                        type: string
        422:
            description: 注册失败
            schema:
                properties:
                    code:
                        type: string
                    message:
                        type: string
    """
    try:
        data = request.get_json()
        data['password'] = User.generate_hash(data['password'])
        user_schema = UserSchema()
        users = user_schema.load(data)
        result = user_schema.dump(users.create())
        return response_with(resp.SUCCESS_201)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@users_bp.route('/login', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        current_user = User.find_by_username(data['username'])
        if not current_user:
            return response_with(resp.SERVER_ERROR_404)
        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            return response_with(resp.SUCCESS_201,value={'message': 'Logged in as {}'.format(current_user.username),
              "token": access_token,"name":current_user.username,"avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'})
        else:
            return response_with(resp.UNAUTHORIZED_401)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
