# pip install flask
# Flask is a class in module flask
# render_template is used to get render html pages
from flask import Flask , render_template 
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime


# create an instance of Flask
app=Flask(__name__)
app.config['SECRET_KEY']='secret' 
# this secret key should be provided by environmental variables for practical purposes to maintain security

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=SQLAlchemy(app)



from routes import *
#this is equivalent to writing all the code in the routes.py file here.
#So the placement of the code is important



if __name__=='__main__' :

    app.run(debug=True)



