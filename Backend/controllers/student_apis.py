from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import utils, auth_token_required, roles_required
from controllers.database import db
from controllers.models import *


class get_company_list(Resource):
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
    
class company_drive_list(Resource):
    def get(self, company_id):
        drives = PlacementDrive.query.filter_by(company_id=company_id).all()
        
        drive_list = []
        for drive in drives:
            drive_data = {
                'id': drive.id,
                'job_title': drive.job_title,
                'job_description': drive.job_description,
                'branch': drive.branch,
                'min_cgpa': drive.min_cgpa,
                'status': drive.status
            }
            drive_list.append(drive_data)
        
        return make_response(jsonify({'drives': drive_list}), 200)