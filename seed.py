from app import db 
from models import Pet

db.drop_all()
db.create_all()

# # Google Drive creates a public url of images with the below link and a unique ID concatenated on
# drive_url = "https://drive.usercontent.google.com/download?id="
# Luna url: https://drive.usercontent.google.com/download?id=1AHYCk1KxFDZCluaOZR0CEd38k0F-9qZM

dog1 = Pet(name="Luna", species="dog", photo_url="../static/images/luna.jpg", age=3, notes="Sheds a lot, very sassy, good girl.", available=False)
dog2 = Pet(name="Champion", species="dog", photo_url="../static/images/champ.jpg", age=12, notes="Hyper, frantic, very loving, good boy", available=False)
dog3 = Pet(name="Snowball", species="dog", photo_url="../static/images/snowball.jpg", age=12, notes="Sometimes referred to as Snownuts, feral (at times), a big ball of fur, very cute, good girl.", available=False)
cat = Pet(name="Stanky", species="cat", photo_url="../static/images/stanky.jpeg", age=3, notes="Big eyes, affectionate, minds her own business, good girl.")


db.session.add_all([dog1, dog2, dog3, cat])
db.session.commit()
# flask-wtforms-adoption-agency/static/images/luna.jpg
# /Users/jonathancheng/Springboard/Unit 25 - Flask/flask-wtforms-adoption-agency/static/images/luna.jpg