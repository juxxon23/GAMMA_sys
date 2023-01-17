import random

class User:

    def __init__(self, business_name, business_email, business_password,
                 comercial_activity, plan_type):
        self.business_id = random.randint(1, 100)
        self.business_name = business_name
        self.comercial_activity = comercial_activity
        self.plan_type = plan_type
        self.business_email = business_email
        self.business_password = business_password
 
