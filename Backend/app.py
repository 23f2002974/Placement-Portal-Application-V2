from flask import Flask
from flask_security import Security
from flask_restful import Api

from controllers.database import db
from controllers.config import Config
from controllers.user_datastore import user_datastore
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    security = Security(app, user_datastore)

    api = Api(app, prefix='/api')
    with app.app_context():
        db.create_all()

        admin_role = user_datastore.find_or_create_role(name='admin', description='Administrator')
        student_role = user_datastore.find_or_create_role(name='student', description='Student')
        company_role = user_datastore.find_or_create_role(name='company', description='Company')

        if not user_datastore.find_user(email='admin@gmail.com'):
            user_datastore.create_user(
                email='admin@gmail.com',
                password='admin123',
                roles=[admin_role]
            )

        db.session.commit()

    return app, api

app, api = create_app()

CORS(app, origins=['http://localhost:5173','http://127.0.0.1:5000'])

@app.route('/celery')
def example():
    from celery_app import example_task
    example_task.delay()
    return "Task has been triggered!"
@app.route('/send-email')
def send_email_route():
    from celery_app import send_welcome_email
    to_email = 'udit@placementportal.com'
    send_welcome_email.delay(to_email)
    return "Email has been sent!"

from controllers.auth_apis import LoginApi, LogoutApi, RegisterApi


api.add_resource(LoginApi, '/login')
api.add_resource(LogoutApi, '/logout')
api.add_resource(RegisterApi, '/register')

from controllers.admin_apis import GetCompanyListApi, ApproveCompanyApi, RejectCompanyApi, GetPendingCompanyListApi
api.add_resource(GetCompanyListApi, '/companies')
api.add_resource(ApproveCompanyApi, '/companies/<int:company_id>')

from controllers.student_apis import get_company_list, company_drive_list
api.add_resource(get_company_list, '/student/companies')
api.add_resource(company_drive_list, '/student/companies/<int:company_id>/drives')

if __name__ == '__main__':
    app.run(debug=True)