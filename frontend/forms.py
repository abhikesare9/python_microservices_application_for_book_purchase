
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SearchField,HiddenField,IntegerField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit   = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit   = SubmitField('Login')

class ItemForm(FlaskForm):
    book_id = HiddenField(validators=[DataRequired()])
    quatity = HiddenField(validators=[DataRequired()])



