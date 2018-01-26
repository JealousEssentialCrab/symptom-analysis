from flask import Flask
from symptoms.api import symptoms_api
from symptoms.flask_utils import EntityEncoder


def create_app():
    app = Flask(__name__)

    app.register_blueprint(symptoms_api.symptoms, url_prefix="/symptoms")
    app.register_blueprint(symptoms_api.diagnoses, url_prefix="/diagnoses")
    app.json_encoder = EntityEncoder
    return app


app = create_app()


@app.route('/')
def hello_world():
    return app.send_static_file("index.html")
