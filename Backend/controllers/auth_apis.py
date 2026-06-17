from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import utils, auth_token_required, roles_required
from controllers.user_datastore import user_datastore
from controllers.database import db

class LoginApi(Resource):
    def post(self):
        
        login_credentials = request.get_json()
        if not login_credentials:
            return make_response(jsonify({'error': 'Invalid input'}), 400)
        
        email = login_credentials.get('email', None)
        password = login_credentials.get('password', None)

        if not email or not password:
            return make_response(jsonify({'error': 'Email and password are required'}), 400)
        

        user = user_datastore.find_user(email=email)

        if not user or not utils.verify_password(password, user.password):
            return make_response(jsonify({'error': 'Invalid email or password'}), 401)
        
        auth_token = user.get_auth_token()
        utils.login_user(user)

        respone = {
            'message': 'Login successful',
            'user': {
                'email': user.email,
                'role': [role.name for role in user.roles],
                'auth_token': auth_token
            },
        }

        return make_response(jsonify(respone), 200)
        

class LogoutApi(Resource):
    @auth_token_required
    def post(self):
        utils.logout_user()
        return make_response(jsonify({'message': 'Logout successful'}), 200)
    


class RegisterApi(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'Invalid input'}), 400)
        
        email = data.get('email', None)
        password = data.get('password', None)
        role = data.get('role', None)

        if not email or not password or not role:
            return make_response(jsonify({'error': 'Email, password, and role are required'}), 400)
        
        if '@' not in email or '.' not in email.split('@')[-1]:
            return make_response(jsonify({'error': 'Invalid email format'}), 400)
        
        if user_datastore.find_user(email=email):
            return make_response(jsonify({'error': 'Email already registered'}), 400)
        
        user_role = user_datastore.find_role(role)
        if not user_role:
            return make_response(jsonify({'error': 'Invalid role specified'}), 400)

        new_user = user_datastore.create_user(
            email=email,
            password=utils.hash_password(password),
            roles=[user_role]
        )

        db.session.commit()

        response = {
            'message': 'User registered successfully',
            'user': {
                'email': new_user.email,
                'roles': [role.name for role in new_user.roles]
            }
        }

        return make_response(jsonify(response), 201)