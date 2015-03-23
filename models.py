from app import db

class Element(db.Model):
    atomic_number = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(3))
    name = db.Column(db.String(50))
    atomic_mass = db.Column(db.Integer)
    history = db.Column(db.Text)
    group = db.Column(db.Integer, db.ForeignKey('group.column'))
    period = db.Column(db.Integer, db.ForeignKey('period.row'))
  	
  	def __init__(self, atomic_number, symbol, name, atomic_mass, group, period,history="None"):
        self.atomic_number = atomic_number
        self.symbol = symbol
        self.name = name
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.period = period
        self.history = history


    def __repr__(self):
        return '<Element %s>' % self.symbol

class Period(db.Model):
    row = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    properties = db.Column(db.Text)
    elements = db.relationship('Element',backref='period',lazy='dynamic')
  	#trivias = db.relationship('Trivia',backref='period',lazy='dynamic')

  	def __init__(self, row, description="None", properties="None"):
  		self.row = row
  		self.description = description
  		self.properties = properties

    def __repr__(self):
        return '<Period %s>' % self.symbol

class Group(db.Model):
    column = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    information = db.Column(db.Text)
    elements = db.relationship('Element',backref='group',lazy='dynamic')
    #trivias = db.relationship('Trivia',backref='group',lazy='dynamic')
  	
  	def __init__(self, column,name, description="None", properties="None"):
  		self.column = column
  		self.name = name
  		self.description = description
  		self.properties = properties

    def __repr__(self):
        return '<Group %s>' % self.name

