# forms
from  flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of owner: ')
    pup_id = IntegerField('Id number of puppy to assign owner: ')
    submit = SubmitField('Add owner')