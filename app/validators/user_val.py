from marshmallow import Schema, fields, validate

class RegisterUser(Schema):
    businessName = fields.String(required=True, validate=validate.Length(min=3,max=30))
    comercialActivity = fields.String(required=True, validate=validate.Length(min=10,max=40))
    businessEmail = fields.String(required=True, validate=validate.Length(min=13,max=60))
    businessPassword = fields.String(required=True, validate=validate.Length(min=8,max=20))
    planType = fields.Integer(required=True) # En una prueba acepto string

class LoginUser(Schema):
    businessEmail = fields.String(required=True, validate=validate.Length(min=13,max=60))
    businessPassword = fields.String(required=True, validate=validate.Length(min=8,max=20))
