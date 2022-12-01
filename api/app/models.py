from app import db
from mongoengine import *


class Employee(Document):
    id = StringField(required=True)
    first_name = StringField(required=True, max_length=200)
    last_name = StringField(max_length=200)
    salary = FloatField(min_value=0)
    absent_days = IntField(min_value=0)
    parental_leaves = IntField(min_value=0)
    overtime = IntField(min_value=0)


class EngineeringManager(Document):
    id = StringField(required=True)
    name = StringField(max_length=200)
    team_salary = FloatField(min_value=0)
    acces_authorization = ListField(max_length=1000)
    production_process = ListField(max_length=1000)
    job_status = StringField(max_length=200)


class External(Document):
    id = StringField(required=True)
    name = StringField(max_length=200)
    providers = StringField(max_length=200)
    company_type = StringField(max_length=200)
    accounting = FloatField(min_value=0)