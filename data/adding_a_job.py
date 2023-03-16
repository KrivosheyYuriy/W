from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    team_leader = IntegerField('Team leader', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    is_finished = BooleanField("Is job finished?")

    submit = SubmitField('Submit')