from app import db

class Element(db.Model):
    atomic_number = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(3))
    name = db.Column(db.String(50))
    atomic_mass = db.Column(db.Integer)
    history = db.Column(db.Text)
    group = db.Column(db.Integer, db.ForeignKey('group.column'))
    period = db.Column(db.Integer, db.ForeignKey('period.row'))
  	
  	def __init__(self, atomic_number, symbol, name, atomic_mass, group, period,history=None):
        self.atomic_number = atomic_number
        self.symbol = symbol
        self.name = name
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.period = period

    def __repr__(self):
        return '<Element %s>' % self.symbol