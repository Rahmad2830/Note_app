from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
  username = StringField('Username', [DataRequired(), Length(min=3)])
  password = StringField('Password', [DataRequired(), Length(min=3)])
  submit = SubmitField('login')
  
class RegisterForm(FlaskForm):
  username = StringField('Username', [DataRequired(), Length(min=3)])
  password = StringField('Password', [DataRequired(), Length(min=3)])
  confirm_password = StringField('Confirm Password', [DataRequired(), EqualTo('password', message='password must be match')])
  submit = SubmitField('login')
  
class NoteForm(FlaskForm):
  note = TextAreaField('Catatan')
  submit = SubmitField('Tambah')
  
class EditForm(FlaskForm):
  notes = TextAreaField('Catatan')
  submit = SubmitField('Simpan')