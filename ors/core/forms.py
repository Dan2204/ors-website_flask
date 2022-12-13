from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email


class FreeQuoteForm(FlaskForm):

    name = StringField('Name: ', validators=[DataRequired()])
    company_name = StringField('Company Name: ')
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    phone = StringField('Contact Number: ', validators=[DataRequired()])
    comments = TextAreaField('Comments: ')
    submit = SubmitField('Submit')


class FullContactForm(FlaskForm):

    company_name = StringField('Company Name: ', validators=[DataRequired()])
    number_of_staff = StringField('Number of staff: ')
    move_date = StringField('Expected move date: ')
    address = StringField('Address: ', validators=[DataRequired()])
    name = StringField('Name: ', validators=[DataRequired()])
    phone = StringField('Contact Number: ', validators=[DataRequired()])
    mobile = StringField('Mobile Number: ')
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    message = TextAreaField('Message: ')
    submit = SubmitField('Submit')
