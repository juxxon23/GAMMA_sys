from app.db.model import db


class DBTool:

    def add(self, *args):
        try:
            for new in args:
                db.session.add(new)
                print('hello')
                db.session.commit()
            return 'ok'
        except Exception as ex:
            error_msg = {'exception': 'dbtool_add', 'ex': str(ex)}


    def update(self):
        try:
            db.session.commit()
            return 'ok'
        except Exception as ex:
            error_msg = {'exception': 'dbtool_update', 'ex': str(ex)}


    def delete(self, obj):
        try:
            db.session.delete(obj)
            db.session.commit()
            return 'ok'
        except Exception as ex:
            error_msg = {'exception': 'dbtool_delete', 'ex': str(ex)}


    def get_all(self, table_name):
        try:
            data = db.session.query(table_name).all()
            return data
        except Exception as ex:
            error_msg = {'exception': 'dbtool_get_all', 'ex': str(ex)}


    def get_by_email(self, table_name, value):
        try:
            data = db.session.query(table_name).filter_by(business_email=value).first()
            return data
        except Exception as ex:
            error_msg = {'exception': 'dbtool_get_by_email', 'ex': str(ex)}
