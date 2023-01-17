import json

class JSONTool:

    file_name = 'user_db.json'

    def load(self):
        with open(self.file_name) as data_json:
            data = json.load(data_json)
            return data
    

    def write(self, ndata):
        # ndata : User
        content_dict = {
                    'business_name' : ndata.business_name,
                    'business_email' : ndata.business_email, 
                    'business_password' : ndata.business_password, 
                    'comercial_activity' : ndata.comercial_activity, 
                    'plan_type' : ndata.plan_type
                    }
        with open(self.file_name, 'w') as data_json:
            data = json.dump(content_dict, data_json)
            return data
