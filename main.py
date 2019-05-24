from flask import Flask, jsonify, render_template
from flask_restful import Api, Resource, reqparse
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json

app = Flask(__name__)
api = Api(app)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per second"],
)

number_of_users = 65536
users = {}

#pętla generująca słownik z 1-number_of_users uzytkowników (user_id)
for a in range(1,number_of_users):
    users[a] = ({'user_id': a, 'counter': 0})

class User(Resource):
    
#funckja renderująca stronę domową
    @app.route('/')
    def home():
        return render_template('home.html')

#wyświetlanie JSON {'user_id': , 'counter': }
    def get(self, user_id):
        id = user_id
        if 0 < id < number_of_users:
            string_to_json = json.dumps(users.get(id))
            loaded_string_to_json = json.loads(string_to_json)
            return loaded_string_to_json, 200
        else:
            return "Musisz wpisac liczbe od 1 do 65535", 422

#licznik oparty na słowniku
    @app.route('/user/<user_id>/counter')
    def counter(user_id):
        id = int(user_id)
        if users[id]['counter'] < 1024:
            users[id]['counter'] += 1
        else:
            return "Osiągnieto maksymalną wartość licznika = 1024", 501
        return "Pomyślna inkrementacja", 200

#resetowanie licznika wszystkich <user_id>
    @app.route('/reset')
    def reset():
        for b in range(1,number_of_users):
            users[b]['counter'] = 0
        return "Licznik zresetowany", 200

api.add_resource(User, "/user/<int:user_id>")
app.run(debug=True)
