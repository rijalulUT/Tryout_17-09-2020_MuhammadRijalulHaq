from app import db
from datetime import datetime

class Prodis(db.Model):
    id          = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    nama_prodi  = db.Column(db.String(140),nullable=False)
    created_at  = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime,default=datetime.utcnow)
    mahasiswas  = db.relationship("Mahasiswas",
                                  lazy    ='select',
                                  backref =db.backref('mahasiwas',lazy ='joined'))
def __repr__(self):
        return '<Mahasiswa {}>'.format(self.name)