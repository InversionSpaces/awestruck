from awestruck import db

class User(db.Model):
    id       = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    login    = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)

    is_authenticated = True
    is_active        = True
    is_anonymous     = False

    def __init__(self, login):
        self.login = login

    def save(self, password):
        self.password = password
        db.session.add(self)
        db.session.commit()

    def check_pass(self, password):
        return self.password == password

    def get_id(self):
        return str(self.id).encode("utf-8").decode("utf-8") 
    
    @staticmethod
    def get(uid):
        return User.query.get(uid)

    
