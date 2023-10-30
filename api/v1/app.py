#!/usr/bin/python3
"""
"""
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response, render_template, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# flask server environmental setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

# create a CORS instance
cors = CORS(app, resources={r'/*': {'origins': host}})

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    # method to handle @app.teardown_appcontext that calls storage.close()
    storage.close()

if __name__ == "__main__":
    # initializes global error handling
    setup_global_errors()
    # start Flask app
    app.run(host=host, port=port)
