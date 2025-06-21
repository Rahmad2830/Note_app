from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
  username = StringField('Username', [DataRequired(), Length(min=3)])
  password = PasswordField('Password', [DataRequired()])
  submit = SubmitField('Login')
  
class RegisterForm(FlaskForm):
  username = StringField('Username', [DataRequired(), Length(min=3)])
  password = PasswordField('Password', [DataRequired(), Length(min=3)])
  confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password', message='password must be match')])
  submit = SubmitField('Register')
  
class NoteForm(FlaskForm):
  note = TextAreaField('Catatan')
  submit = SubmitField('Tambah')
  
class EditForm(FlaskForm):
  notes = TextAreaField('Catatan')
  submit = SubmitField('Simpan')