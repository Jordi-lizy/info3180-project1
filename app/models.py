from . import db

class PropertyProfile(db.Model):

    _tablename_ = 'property_profile'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String())
    description = db.Column(db.String())
    numofbedrooms = db.Column(db.String())
    numofbathrooms=db.Column(db.String())
    price = db.Column(db.String())
    ptype = db.Column(db.String())
    location = db.Column(db.String())
    photo = db.Column(db.String())
    
    def __init__(self, title, description, numofbedrooms, numofbathrooms, price, ptype, location, photo):
        self.title=title
        self.description=description
        self.numofbedrooms=numofbedrooms
        self.numofbathrooms=numofbathrooms
        self.price=price
        self.ptype=ptype
        self.location=location
        self.photo=photo