from app import db
from datetime import datetime 
from app.model.prodi import Prodis
class Mahasiswas(db.Model):
    id                  = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    nim                 = db.Column(db.String(11),nullable=False)
    name                = db.Column(db.String(230),nullable=False)
    tgl_lahir           = db.Column(db.String(10),nullable=False)
    ibu                 = db.Column(db.String(230),nullable=False)
    email               = db.Column(db.String(120),index=True,unique=True,nullable=False)
    created_ats          = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at          = db.Column(db.DateTime,default=datetime.utcnow)
    prodi_id            = db.Column(db.BigInteger,db.ForeignKey(Prodis.id))
    prodis              = db.relationship("Prodis",backref="prodi_id")
    
    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.name)
    
    # def setPassword(self,password):
    #     self.password = generate_password_hash(password)