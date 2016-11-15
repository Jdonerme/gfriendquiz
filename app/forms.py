from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired

class IndexForm(Form):
	startButton = SubmitField("Take the quiz")
class LoginForm(Form):
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)
   
class Question(Form):
	response = RadioField('Response', choices = [(0, ''), (1, ''), (2, ''), (3, ''), (4, ''), (5, "")], \
									  validators=[DataRequired()])
		                                                 
 
class Result(Form):
	again = SubmitField('Take it again:')