from flask import Flask
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class UserAPI(Resource):
    def get(self, id=None):
        return self.__dict__, 200

    def put(self, id):
        pass

    def delete(self, id=None):
        pass


api.add_resource(UserAPI, '/api/v1.0/user/<int:id>', endpoint='user')
api.add_resource(UserAPI, '/api/v1.0/user', endpoint='users')

if __name__ == '__main__':
    app.run(debug=True)
