#this module contains all the routes for the app

from app import app
from flask import render_template # render_template is used to get render html pages
import forms # this imports the forms.py code here
# this tells the app that at '/' we need to run index()
@app.route('/') #this is the decorator to the function index()
@app.route('/index') # you can add more than one routes 
def index():
    return render_template('index.html',current_title='NEW TITLE') # here you can add the required html and pass values to the html . We can use {{ }} to use passed values in the html file

@app.route('/about', methods=['GET','POST'])
def about():
    form=forms.AddTaskForm() # this creates instance of class AddTaskForm 
    
    if form.validate_on_submit():
        print('Submitted data :',form.title.data)
        return render_template('about.html',form=form ,title=form.title.data)

    return render_template('about.html',form=form) # the from is passed to the page using form variable