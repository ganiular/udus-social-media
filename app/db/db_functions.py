import os

env = os.environ.get('FLASK_ENV', 'production')
if env == 'development':
    from app.db.sqlite_functions import *
else:
    from app.db.mysql_functions import *