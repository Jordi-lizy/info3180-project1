from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SelectField 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, DataRequired, Length


selection_type = [('House', 'House'), ('Apartment', 'Apartment')]

class NewPropertyForm(FlaskForm):
    title = TextField('Property Title', validators=[DataRequired()])
    numofbedrooms = TextField('No. of Rooms', validators=[DataRequired()])
    numofbathrooms = TextField('No. of Bathrooms', validators=[DataRequired()])
    location = TextField('Location', validators=[DataRequired()])
    price = TextField('Price', validators=[DataRequired()])
    ptype = SelectField('Property Type', choices=selection_type)
    description = TextAreaField('Property Description', validators=[DataRequired()])
    photo = FileField('File', validators=[FileRequired(), 
    FileAllowed(['jpg', 'png', 'jpeg'], 'Images Only!')])