from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday=db.Column(db.DateTime)

    animals = db.relationship('Animal', backref='zookeeper')

    def __repr__(self):
        return f'<ID: {self.id}>, '\
        + f'<Name: {self.name}>, '\
        + f'<Birthday: {self.birthday}>, '\
        + f'<Animal: {self.animals}>, '

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship('Animal', backref='enclosure')

    def __repr__(self):
        return f'<ID: {self.id}>, '\
        + f'<Environment: {self.environment}>, '\
        + f'<Open to Visitors: {self.open_to_visitors}>, '\
        + f'<Animal: {self.animals}>, '
    
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    def __repr__(self):
        return f'<ID: {self.id}>, '\
        + f'<Name: {self.name}>, '\
        + f'<Species: {self.species}>, '\
        + f'<Zookeeper: {self.zookeeper}>, '\
        + f'<Enclosure: {self.enclosure}>, '
    
