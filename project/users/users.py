class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_plaintext = db.Column(db.String, nullable=False)

    def __init__(self, email, password_plaintext):
        self.email = emali
        self.password_plaintext = password_plaintext

    def __repr__(self):
        return '<User {0}'.format(self.name)

