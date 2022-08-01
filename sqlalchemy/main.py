from ctypes import addressof
from enum import auto
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(filename)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s")
# log = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)
# ---------------use logging to improve the code

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345@localhost:5432/fastapi"

Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


session = sessionLocal()

class Users(Base):
    __tablename__ = "new_users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(30))
    address = Column(String(50), nullable=False)

Base.metadata.create_all(engine)

# u = [Users(name="abhay",email="rathod.abh@gmail.com",address="dfsb"),Users(name="abhay2",email="fjsdjv",address="sdbshdhsdv")]
# session.add_all(u)
# session.commit()
# session.close()


a = session.query(Users).all()
for i in a:
    print("name",i.name, "email",i.email, "address", i.address)

b = session.query(Users).filter(Users).scalar()         # may give error if more than one field is present
b = session.query(Users).filter(Users.id==1).scalar()      #no error kyuki filter karke sirf ek result aayega
print(b.name)