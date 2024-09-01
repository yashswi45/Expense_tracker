from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Up!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

class ExpenseForm(FlaskForm):
    amount = FloatField("Amount", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    date = DateField("Date", format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField("Add Expense")

