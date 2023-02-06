class ExceptionHandler:

    def wrap(self, exc):
        if exc is None:
            msg = {'status': 'user', 'msg': 'The user doesn\'t exists'}
        elif type(exc) == dict:
            msg = {'status': exc['exception'], 'ex': exc['ex']}
        else:
            msg = {'status': 'ok'}
        return msg
