from marshmallow import Schema

class RegisterUser(Schema):
    business_name = ''
    comercial_activity = ''
    business_email = ''
    business_password = ''
    plan_type = ''

class LoginUser(Schema):
    business_email = ''
    business_password = ''
