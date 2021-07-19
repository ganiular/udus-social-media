import click, os
from flask import current_app, g
from flask.cli import with_appcontext

env = os.environ.get('FLASK_ENV', 'production')

if env == 'development':
    import sqlite3

    def get_db():
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config["DATABASE"],
                detect_types=sqlite3.PARSE_DECLTYPES 
                # it convert each culumn to his suitable type
            )
            g.db.row_factory = sqlite3.Row

        return g.db

    def close_db(e=None):
        db = g.pop('db', None)

        if db is not None:
            db.close()
            print('db closed')
        else:
            print('db close_db already')

    def init_db():
        db = get_db()

        with current_app.open_instance_resource('schema.sql') as f:
            db.executescript(f.read().decode("utf-8"))

    @click.command('init-db')
    @with_appcontext
    def init_db_command():
        "command line interface call of 'init-db' to execute this block"
        init_db()
        click.echo("Database Intitialized")

    def register_with_app(app):
        app.teardown_appcontext(close_db) # close_db is run after every response
        app.cli.add_command(init_db_command) # add cmd line interface to flask

else:
    from flask_mysqldb import MySQL

    def get_db():
        if 'db' not in g:
            g.db = MySQL().connection

        return g.db

    def close_db(e=None):
        db = g.pop('db', None)

        if db is not None:
            db.close()
            print('db closed')
        else:
            print('db close_db already')

    def init_db():
        db = get_db().cursor()

        with current_app.open_instance_resource('mysql_schema.sql') as f:
            for statement in f.read().decode("utf-8").split(';'):
                if statement:
                    print(statement)
                    db.execute(statement)
            db.close()

    @click.command('init-db')
    @with_appcontext
    def init_db_command():
        "command line interface call of 'init-db' to execute this block"
        init_db()
        click.echo("Database Intitialized")

    def register_with_app(app):
        # register or login to database
        app.config['MYSQL_HOST'] = 'tboard.mysql.pythonanywhere-services.com'
        app.config['MYSQL_USER'] = 'tboard'
        app.config['MYSQL_PASSWORD'] = 'DEVELOPERpw#db'
        app.config['MYSQL_DB'] = 'tboard$mysql_tboard_db'
        app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
        
        # register function that close database after every response
        # function already registered in flask_mysqldb.py
        app.teardown_appcontext(close_db)

        # register function that initialize database when call from cmd line
        app.cli.add_command(init_db_command)

    