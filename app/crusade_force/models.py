from app import db


class CrusadeForce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    faction = db.Column(db.String(50), nullable=False)
    supply_limit = db.Column(db.Integer, default=50)

    def __repr__(self):
        return f'<CrusadeForce {self.name}>'
