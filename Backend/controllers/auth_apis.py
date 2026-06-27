from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import utils, auth_token_required, roles_required
from controllers.user_datastore import user_datastore
from controllers.database import db
from flask import request
from .models import User, Student, Company
from flask_restful import Resource
from werkzeug.utils import secure_filename
import os

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
    


class StudentRegisterApi(Resource):
    def post(self):

        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return {"error": "Email and password are required"}, 400

        if user_datastore.find_user(email=email):
            return {"error": "Email already exists"}, 400

        role = user_datastore.find_role("student")

        user = user_datastore.create_user(
            email=email,
            password=utils.hash_password(password),
            roles=[role]
        )

        db.session.flush()

        # Resume upload
        resume = request.files.get("resume")
        resume_path = None

        if resume:
            filename = secure_filename(resume.filename)

            upload_folder = os.path.join("uploads", "resumes")
            os.makedirs(upload_folder, exist_ok=True)

            resume_path = os.path.join(upload_folder, filename)
            resume.save(resume_path)

        student = Student(
            user_id=user.id,
            full_name=request.form.get("full_name"),
            branch=request.form.get("branch"),
            cgpa=float(request.form.get("cgpa")),
            graduation_year=int(request.form.get("graduation_year")),
            phone=request.form.get("phone"),
            resume_url=resume_path      # add this column if needed
        )

        db.session.add(student)
        db.session.commit()

        return {
            "message": "Student registered successfully",
            "resume_uploaded": bool(resume)
        }, 201
    
class CompanyRegisterApi(Resource):
    def post(self):
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        if user_datastore.find_user(email=email):
            return {"error": "Email already exists"}, 400

        role = user_datastore.find_role("company")

        user = user_datastore.create_user(
            email=email,
            password=utils.hash_password(password),
            roles=[role]
        )

        db.session.flush()

        company = Company(
            user_id=user.id,
            name=data["companyName"],
            website=data.get("website"),
            description=data.get("description")
        )

        db.session.add(company)
        db.session.commit()

        return {
            "message": "Company registered successfully"
        }, 201