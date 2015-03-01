from . import db 

class User(db.Model):
  id = db.Column(db.Integer, primary_key = 'True')
  firstname = db.Column(db.String(80))
  lastname = db.Column(db.String(80))
  pimage =  db.Column(db.String(80))
  sex = db.Column(db.String(80))
  age = db.Column(db.Integer)
  
  def __init__(self, firstname,lastname,pimage,sex,age):
    self.firstname = firstname
    self.lastname = lastname
    self.pimage = pimage
    self.sex = sex
    self.age = age

    
    
  def __repr__(self):
    return'<User%r>'%self.firstname