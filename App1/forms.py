from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo,ValidationError
from server import History

class RegistrationForm(FlaskForm):
    userName = StringField('Username',
                            validators=[DataRequired(),
                                        Length(min=3,max=10)])
    # email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5)])
    confirm_password = PasswordField('Password',
                                    validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('SignUp')

    def validate_username(self,userName):
        user = User.query.filter_by(userName=userName.data)
        if user:
            raise ValidationError('Err! That username is taken! ')
    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Err! That email is taken! ')

class LoginForm(FlaskForm):
    email = StringField('userName',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# class UpdateAccountForm(FlaskForm):
#     userName = StringField('Username',
#                             validators=[DataRequired(),
#                                         Length(min=3,max=10)])
#     email = StringField('Email',validators=[DataRequired(),Email()])
#     picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
#     submit = SubmitField('Update!')
#
#
#     def validate_username(self,userName):
#         if userName.data != current_user.userName:
#             user = User.query.filter_by(userName=userName.data)
#             if user:
#                 raise ValidationError('Err! That username is taken! ')
#     def validate_email(self,email):
#         if email.data != current_user.email:
#             email = User.query.filter_by(email=email.data).first()
#             if email:
#                 raise ValidationError('Err! That email is taken! ')
#
#
# class PostForm(FlaskForm):
#     title = StringField('Title',validators=[DataRequired()])
#     content = TextAreaField('Content',validators=[DataRequired()])
#     submit = SubmitField('Post')
