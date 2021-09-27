import argparse
from os import abort
from worker.start_service import start_service
from worker.setup_db import setup_db
from sanic import Sanic
from sanic_cors import CORS
from rethinkdb import RethinkDB
from rethinkdb.errors import RqlDriverError
from sanic.response import text
from blueprint.notice_blueprint import notice_blueprint
from blueprint.product_blueprint import product_blueprint
from blueprint.consumer_blueprint import consumer_blueprint
from blueprint.payment_blueprint import payment_blueprint
from blueprint.order_blueprint import order_blueprint
from blueprint.report_blueprint import report_blueprint
from blueprint.adminstrator_blueprint import adminstrator_blueprint
import firebase_admin
# Setting up the databse
r = RethinkDB()

# Database connection details
db_config = {
    'DB_HOST': 'localhost',
    'DB_PORT': 28015,
    'DB_NAME': 'eshemachoch',
}


# Setting up the server
app = Sanic("eshemachoch", load_env='ESHEMACHOCH_')
app.config.update(db_config)
CORS(app, automatic_options=True)
app.ctx.firebase = firebase_admin.initialize_app()

# Adding route handlers
app.blueprint(notice_blueprint)
app.blueprint(product_blueprint)
app.blueprint(consumer_blueprint)
app.blueprint(order_blueprint)
app.blueprint(report_blueprint)
app.blueprint(payment_blueprint)
app.blueprint(adminstrator_blueprint)


@app.before_server_start
def connect_db(app, _):
    try:
        # Connecting to the app database
        conn = r.connect(
            host=app.config.DB_HOST, port=app.config.DB_PORT, db=app.config.DB_NAME)
        app.ctx.conn = conn
        # Starting the application services
        start_service(app)
    except RqlDriverError:
        print(503, "No app database connection could be established.")
        abort()


@app.before_server_stop
def close_db(app, _):
    try:
        # Closing the database connection
        app.ctx.conn.close()
    except AttributeError:
        pass


# Starting the server
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--setup', action="store_true")
    args = parser.parse_args()
    if args.setup:
        setup_db(app.config, r)

    app.run(host="0.0.0.0", port=8000)
    # app.run()
