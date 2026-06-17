from controllers.database import db
from datetime import datetime

from flask_security import UserMixin, RoleMixin

class User(db.Model, UserMixin ):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    fs_token_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    roles = db.relationship('Role', secondary='user_roles') 


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'), nullable=False)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), unique=True, nullable=False)

    full_name = db.Column(db.String(120), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    cgpa = db.Column(db.Float, nullable=False)
    graduation_year = db.Column(db.Integer, nullable=False)

    phone = db.Column(db.String(20))
    resume_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    applications = db.relationship('Application', backref='student', cascade='all, delete')


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), unique=True, nullable=False)

    name = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255))
    description = db.Column(db.Text)
    approved = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    drives = db.relationship('PlacementDrive', backref='company', cascade='all, delete')


class PlacementDrive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'), nullable=False)

    job_title = db.Column(db.String(255), nullable=False)
    job_description = db.Column(db.Text)
    branch = db.Column(db.String(100))
    min_cgpa = db.Column(db.Float)

    deadline = db.Column(db.DateTime)
    status = db.Column(db.String(50), default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    applications = db.relationship('Application', backref='drive', cascade='all, delete')

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    drive_id = db.Column(db.Integer, db.ForeignKey('placement_drive.id', ondelete='CASCADE'), nullable=False)

    status = db.Column(db.String(50), default="applied")
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)

    interview = db.relationship('Interview', backref='application', uselist=False)

    __table_args__ = (db.UniqueConstraint('student_id', 'drive_id', name='unique_application'),)


class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id', ondelete='CASCADE'), nullable=False)

    interview_date = db.Column(db.DateTime)
    interview_type = db.Column(db.String(50)) 
    result = db.Column(db.String(50)) 

class Placement(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'), nullable=False)
    drive_id = db.Column(db.Integer, db.ForeignKey('placement_drive.id', ondelete='CASCADE'))

    position = db.Column(db.String(255))
    salary = db.Column(db.Float)
    joining_date = db.Column(db.Date)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)