from database import db


class Reserva (db.Model):

    __tablename__ = 'reserva'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    restaurante_id = db.Column(db.Integer, nullable=False)
    reservation_date = db.Column(db.DataTime, nullable=False)
    num_guests = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, restaurante_id, reservation_date, num_guests, special_requests, status):
        self.user_id = user_id
        self.restaurante_id = restaurante_id
        self.reservation_date = reservation_date
        self.num_guests = num_guests
        self.special_requests = special_requests
        self.status = status


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Reserva.query.all()

    @staticmethod
    def get_by_id(id):
        return Reserva.query.get(id)
    
    def update(self, user_id=None, restaurante_id=None, reservation_date=None, num_guests=None, special_requests=None, status=None):
        if user_id is not None:
            self.user_id = user_id
        if restaurante_id is not None:
            self.restaurante_id = restaurante_id
        if reservation_date is not None:
            self.reservation_date = reservation_date
        if num_guests is not None:
            self.num_guests = num_guests
        if special_requests is not None:
            self.special_requests = special_requests
        if status is not None:
            self.status = status

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()