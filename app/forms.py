# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    poster = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])