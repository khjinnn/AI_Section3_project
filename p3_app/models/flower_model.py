from p3_app import db

class Flower(db.Model):
    __tablename__ = 'flower'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    att1 = db.Column(db.Float, nullable=False)
    att2 = db.Column(db.Float, nullable=False)
    att3 = db.Column(db.Float, nullable=False)
    att4 = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Flower {self.id}'