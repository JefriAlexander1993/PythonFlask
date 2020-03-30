# Servidor
from flask import Flask, request,render_template,escape, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/basedatos/database.db"

UPLOAD_FOLDER = os.path.abspath('static/imgs/')
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


app.jinja_env.trim_blocks= True
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Conexion 1
# from flask_sqlalchemy import SQLAlchemy


#app = Flask(__name__)

#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
#app.config['MYSQL_DATABASE_DB'] = 'pythonflask'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'

@app.route('/')
def login():
   return render_template('auth/login.html')



from homecontroller import  *
from registercontroller import  *
from logincontroller import  *
from contactcontroller import  *
from usercontroller import  *


# settings
app.secret_key = "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0"


# starting the app
if __name__ == "__main__":
   db.create_all()
   app.run(port=3000, debug=True)