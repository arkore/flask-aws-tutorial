import os
# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
flask_pass = os.environ.get('FLASK_DB_PASSWORD', '')
SQLALCHEMY_DATABASE_URI = 'postgresql://flask-test:' + flask_pass + '@busdriver-dev.ciuymosjazoe.ap-southeast-2.rds.amazonaws.com:5432'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
