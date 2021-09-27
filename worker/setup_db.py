from os import abort
from rethinkdb.errors import RqlDriverError, RqlRuntimeError, ReqlOpFailedError


def setup_db(config, r):
    # Setting up the database
    try:
        # Connecting to the database
        conn = r.connect(host=config.DB_HOST, port=config.DB_PORT)
        # Creating the database and tables
        try:
            r.db_create(config.DB_NAME).run(conn)
        except RqlRuntimeError:
            pass
        try:
            r.db(config.DB_NAME).table_create('products').run(conn)
        except ReqlOpFailedError:
            pass
        try:
            r.db(config.DB_NAME).table_create('notices').run(conn)
        except ReqlOpFailedError:
            pass
        try:
            r.db(config.DB_NAME).table_create('orders').run(conn)
        except ReqlOpFailedError:
            pass

        try:
            r.db(config.DB_NAME).table_create('consumers').run(conn)
        except ReqlOpFailedError:
            pass
        try:
            r.db(config.DB_NAME).table_create('adminstrators').run(conn)
        except ReqlOpFailedError:
            pass
        try:
            r.db(config.DB_NAME).table_create('product_images').run(conn)
        except ReqlOpFailedError:
            pass
        try:
            r.db(config.DB_NAME).table_create('consumer_images').run(conn)
        except ReqlOpFailedError:
            pass
        print('Database setup completed. You can now run the app without --setup.')
    except RqlDriverError:
        print(503, "No database connection could be established.")
        abort()
    finally:
        conn.close()
