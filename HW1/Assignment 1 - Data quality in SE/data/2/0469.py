from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date

engine = create_engine("mysql+mysqldb://root:cga3026@localhost:3306/gpoascen_crm", echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Modulos(Base):
    __tablename__ = 'modulos'
    idmodulo = Column(Integer, primary_key=True)
    nombre = Column(String)
    idtitulospermisos = Column(Integer)

    def __init__(self, idmodulo, nombre, idtitulospermisos):
        self.idmodulo = idmodulo
        self.nombre = nombre
        self.idtitulospermisos = idtitulospermisos

#print(type(engine))


#test de conexion
# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

#Create register
#modulo = Modulos(None,"test","1")

# 9 - persists data
#session.add(modulo)

#get data
modulos = session.query(Modulos).all()
modulos = session.query(Modulos).filter(Modulos.idmodulo > 10).all()
modulos = session.query(Modulos).filter(Modulos.nombre.like("%credito%")).all()
modulos = session.query(Modulos).filter(Modulos.nombre.like("%es%")).filter(Modulos.idmodulo > 10).all()

moduloUp = session.query(Modulos).filter(Modulos.nombre == "test").first()


if moduloUp :
    print(str(moduloUp.idmodulo) + "  " + moduloUp.nombre )
    moduloUp.nombre = "Se cambia Con SQLAlchemy"

for modulo in modulos :
    print(modulo.nombre)

# 10 - commit and close session
session.commit()
session.close()