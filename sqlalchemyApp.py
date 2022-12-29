import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine, inspect
from sqlalchemy import select

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    cpf = Column(String(11))
    endereco = Column(String(200))

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String(20), nullable=False)
    agencia = Column(Integer, nullable=False)
    numero = Column(Integer, nullable=False)
    id_cliente = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    saldo = Column(Integer)

    cliente = relationship("Cliente", back_populates="conta")

print(Cliente.__tablename__)

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspector_engine = inspect(engine)
print(inspector_engine.get_table_names())

with Session(engine) as session:
    cliente01 = Cliente(
        name = 'Pedro',
        cpf = '123454678901',
        endereco = 'Rua Um, 100 - São Paulo/SP',
        conta=[Conta(
            tipo = 'Poupança',
            agencia = 1,
            numero = 23456,
            saldo = 1000
        )]
    )
    cliente02 = Cliente(
        name = 'Paulo',
        cpf = '223454678901',
        endereco = 'Rua Dois, 200 - São Paulo/SP',
        conta=[Conta(
            tipo = 'Corrente',
            agencia = 1,
            numero = 45676,
            saldo = 2000
        ),
        Conta(
            tipo = 'Poupança',
            agencia = 1,
            numero = 54355,
            saldo = 3000
        )]
    )

session.add_all([cliente01, cliente02])
session.commit()

stmt = select(Cliente).where(Cliente.name.in_(['Paulo']))
for cliente in session.scalars(stmt):
    print(cliente.name)
    print("conta: " + str(cliente.conta[0].numero))