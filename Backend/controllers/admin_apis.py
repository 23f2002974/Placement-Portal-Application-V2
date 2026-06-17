from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import utils, auth_token_required, roles_required
from controllers.database import db
from controllers.models import *


 

class GetCompanyListApi(Resource):
    @auth_token_required
    @roles_required('admin')
    def get(self):
        companies = Company.query.filter_by(approved = True).all()
        company_list = []
        for company in companies:
            company_data = {
                'id': company.id,
                'name': company.name,
                'description': company.description,
                'website': company.website
            }
            company_list.append(company_data)
        
        return make_response(jsonify({'companies': company_list}), 200)
    
class ApproveCompanyApi(Resource):
    @auth_token_required
    @roles_required('admin')
    def post(self, company_id):
        company = Company.query.get(company_id)
        if not company:
            return make_response(jsonify({'error': 'Company not found'}), 404)
        
        company.approved = True
        db.session.commit()
        return make_response(jsonify({'message': 'Company approved successfully'}), 200)
    
class RejectCompanyApi(Resource):
    @auth_token_required
    @roles_required('admin')
    def post(self, company_id):
        company = Company.query.get(company_id)
        if not company:
            return make_response(jsonify({'error': 'Company not found'}), 404)
        
        db.session.delete(company)
        db.session.commit()
        return make_response(jsonify({'message': 'Company rejected and deleted successfully'}), 200)
    
class GetPendingCompanyListApi(Resource):
    @auth_token_required
    @roles_required('admin')
    def get(self):
        companies = Company.query.filter_by(approved = False).all()
        company_list = []
        for company in companies:
            company_data = {
                'id': company.id,
                'name': company.name,
                'description': company.description,
                'website': company.website
            }
            company_list.append(company_data)
        
        return make_response(jsonify({'companies': company_list}), 200)
    
class GetStudentListApi(Resource):
    @auth_token_required
    @roles_required('admin')
    def get(self):
        students = Student.query.all()
        student_list = []
        for student in students:
            student_data = {
                'id': student.id,
                'full_name': student.full_name,
                'branch': student.branch,
                'cgpa': student.cgpa,
                'graduation_year': student.graduation_year,
                'phone': student.phone,
                'resume_url': student.resume_url
            }
            student_list.append(student_data)
        
        return make_response(jsonify({'students': student_list}), 200)
    
class BlockStudentApi(Resource):
    @auth_token_required
    @roles_required('admin')
    def post(self, student_id):
        student = Student.query.get(student_id)
        if not student:
            return make_response(jsonify({'error': 'Student not found'}), 404)
        
        user = User.query.get(student.user_id)
        user.active = False
        db.session.commit()
        return make_response(jsonify({'message': 'Student blocked successfully'}), 200)
    
class UnblockStudentApi(Resource):
    @auth_token_required
    @roles_required('admin')
    def post(self, student_id):
        student = Student.query.get(student_id)
        if not student:
            return make_response(jsonify({'error': 'Student not found'}), 404)
        
        user = User.query.get(student.user_id)
        user.active = True
        db.session.commit()
        return make_response(jsonify({'message': 'Student unblocked successfully'}), 200)
    
class GetDriveListApi(Resource):
    @auth_token_required
    @roles_required('admin')
    def get(self):
        drives = PlacementDrive.query.all()
        drive_list = []
        for drive in drives:
            drive_data = {
                'id': drive.id,
                'company_name': drive.company.name,
                'position': drive.position,
                'description': drive.description,
                'eligibility_criteria': drive.eligibility_criteria,
                'application_deadline': drive.application_deadline.strftime('%Y-%m-%d')
            }
            drive_list.append(drive_data)
        
        return make_response(jsonify({'drives': drive_list}), 200)

class GetApplicationListApi(Resource):
    @auth_token_required
    @roles_required('admin')
    def get(self):
        applications = Application.query.all()
        application_list = []
        for application in applications:
            application_data = {
                'id': application.id,
                'student_name': application.student.full_name,
                'company_name': application.placement_drive.company.name,
                'position': application.placement_drive.position,
                'status': application.status
            }
            application_list.append(application_data)
        
        return make_response(jsonify({'applications': application_list}), 200)