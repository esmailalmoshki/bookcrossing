from sqlmodel import SQLModel, Session, create_engine

# db_url = "postgresql://postgres:123@localhost/warriors_db"
db_url = "mysql://esmail:12345@localhost:3360/warriors_db"
engine = create_engine(db_url, echo=True)

def init_bd():
  SQLModel.metadata.create_all(engine)

def get_session():
  with Session(engine) as session:
    yield session

