# this module will have all the forms for the webapp eg. login , register etc.

#pip install flask_wtf

from flask_wtf import FlaskForm
# FlaskForm is a class used to make forms in flask

from wtforms import StringField , SubmitField
# StringField is used for text entry and submit field is used for submit buttons
from wtforms.validators import DataRequired

# All forms are extended from FlaskForm in flask
class AddTaskForm(FlaskForm):
    
    title=StringField('Title',validators=[DataRequired()])
    # the DataRequired validator prevents user from submitting empty string . In the string field we can have multiple Validators.
    
    submit=SubmitField('Submit')
    # the SubmitField adds a submit button
    
