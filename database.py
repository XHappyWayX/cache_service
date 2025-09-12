from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://odoo:odoo@db:5432/caching")

engine = create_engine(DATABASE_URL)
# engine = create_engine('postgresql+psycopg2://odoo:odoo@localhost:5432/caching_service', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Payloads(Base):
    __tablename__ = "payloads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    input_text: Mapped[str] = mapped_column(String(255), unique=True)
    output_text: Mapped[str] = mapped_column(String(255) )

Base.metadata.create_all(engine)

class crud():
    def create_payloads(self, input, output):
        payload = Payloads(input_text = input, output_text = output)
        session.add(payload)
        session.commit()
        id = payload.id
        session.close()
        return id

class tools():
    def transformer(self, data):
        combined = []
        for a, b in zip(data.list_1, data.list_2):
            combined.append(a.upper())
            combined.append(b.upper())
        output_str = ''.join(combined)
        return output_str