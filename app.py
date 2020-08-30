# pip install flask
# Flask is a class in module flask
# render_template is used to get render html pages
from flask import Flask , render_template

# create an instance of Flask
app=Flask(__name__)
app.config['SECRET_KEY']='secret'

from routes import *
#this is equivalent to writing all the code in the routes.py file here.
#So the placement of the code is important



if __name__=='__main__' :

    app.run(debug=True)



