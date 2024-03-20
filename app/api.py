from db import configure_database, db
from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api

app = Flask(__name__)
configure_database(app)
db.init_app(app)
api = Api(app)


if __name__ == "__main__":
    load_dotenv()
    app.run(port=8888)
