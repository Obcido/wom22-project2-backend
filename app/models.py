from app import app, db
import datetime


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    cabin = db.Column(db.String(100), nullable=False)
    service_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    order_created = db.Column(db.DateTime)

    def __init__(self, cabin, service_name, date):
        self.cabin = cabin
        self.service_name = service_name
        self.date = date
        self.order_created = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'cabin': self.cabin,
            'service_name': self.service_name,
            'date': self.date,
            'order_created': self.order_created.isoformat()
        }

    @staticmethod
    def get_all():
        results = Order.query.all()
        return [result.json() for result in results]

    @staticmethod
    def get_by_id(order_id):
        return Order.query.filter_by(id=order_id).first()

    @staticmethod
    def delete_by_id(order_id):
        try:
            order = Order.query.filter_by(id=order_id).first()
            if order:
                db.session.delete(order)
                db.session.commit()
                return True
            else:
                return False
        except:
            return False


class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100))
    service_created_at = db.Column(db.DateTime)

    def __init__(self, service_name):
        self.service_name = service_name
        self.service_created_at = datetime.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'service_name': self.service_name,
            'service_created_at': self.service_created_at.isoformat()
        }

    @staticmethod
    def get_all():
        results = Service.query.all()
        return [result.json() for result in results]

    @staticmethod
    def get_by_id(service_id):
        return Service.query.filter_by(id=service_id).first()

    @staticmethod
    def delete_by_id(service_id):
        try:
            service = Service.query.filter_by(id=service_id).first()
            if service:
                db.session.delete(service)
                db.session.commit()
                return True
            else:
                return False
        except:
            return False


with app.app_context():
    db.create_all()
