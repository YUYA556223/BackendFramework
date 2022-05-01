# app starter
from plugins.reflection.activator import Activator
from plugins.reflection.test import Test
from plugins.reflection.module import Module
from plugins.reflection.bindingflags import BindingFlags
from plugins.reflection.type import typeof
from db.models import DB
from flask import Flask
from flask_cors.extension import CORS
from argparse import ArgumentParser
import os
from api import Router
from flask_migrate import Migrate

# Create Flask app and submit CORS setting
app = Flask(__name__)
CORS(app, support_credentials=True)


# Initialize database
DB.initialize(app)

# Resister all routing
Router.activate_all_routes(app)

# Run app
if __name__ == '__main__':
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int,
                            default=int(os.environ.get('PORT', 8000)), help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    arg_parser.add_argument('--host', default='0.0.0.0', help='host')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, host=options.host, port=options.port)
