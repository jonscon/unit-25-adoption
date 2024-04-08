from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()

@app.route('/')
def show_pet_list():
    """Homepage - show all pets."""

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Renders pet form (GET) or handles pet form submission (POST)."""

    form = AddPetForm()

    # Validates submitted form (is it a POST request AND is the CSRF token valid?) or passes instance of form to template 
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data

        # Default picture if user doesn't enter a url
        if photo_url == '':
            photo_url = "https://rb.gy/p3bsam"
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()
        flash(f"Created new pet: name is {name}, species is {species}")
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show details of a pet and edit details if desired."""

    pet = Pet.query.get(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        new_photo_url = form.photo_url.data
        # Use old photo if user doesn't enter a new photo url
        if new_photo_url != '':
            pet.photo_url = new_photo_url
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name}'s details updated.")
        return redirect("/")   
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)

