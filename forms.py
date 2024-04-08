from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange, Length

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators = [InputRequired()])
    species = SelectField("Species", choices = [("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL of Pet", validators = [URL(), Optional()])
    age = IntegerField("Age", validators = [NumberRange(min=0, max=30, message="Age must be between 0 and 30."), Optional()])
    notes = StringField("Any other things we should know about?")

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL of Pet", validators = [URL(), Optional()])
    notes = StringField("Notes", validators = [Optional(), Length(min=10)])
    available = BooleanField("Available?")
