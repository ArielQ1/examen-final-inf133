from database import db

class Usuario(db.Model):

    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)


    def __init__(self, name, email, password, phone, role):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.role = role

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    
    def update(self, name=None, email=None, password=None, phone=None, role=None):
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if role is not None:
            self.role = role

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

