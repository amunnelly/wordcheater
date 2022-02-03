# from http.client import LENGTH_REQUIRED
from tokenize import String
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LettersForm(FlaskForm):
    id = StringField()
    letterfield = StringField(label="enter all the letters on the word-wheel here", validators=[DataRequired()])
    submit = SubmitField(label='submit', validators=[DataRequired()])


class PatternForm(FlaskForm):
    id = StringField()
    patternfield = StringField(label="", validators=[DataRequired()])
    submit = SubmitField(label='submit', validators=[DataRequired()])


class SuperForm(FlaskForm):
    id=StringField()
    letterfield = StringField(label="enter all the letters on the word-wheel here", validators=[DataRequired()])
    patternfield = StringField(label="", validators=[DataRequired()])
    submit = SubmitField(label='submit', validators=[DataRequired()])
