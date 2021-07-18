import os
from flask import Flask, render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'sqlite.db')
    )

    try:
        os.makedirs(app.instance_path)
    except:
        pass
    
    @app.route('/')
    def index():
        return render_template('index.html')

    from . import db
    from . import auth
    db.register_with_app(app)
    app.register_blueprint(auth.bp)
    return app
