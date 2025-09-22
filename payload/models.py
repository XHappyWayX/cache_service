from database import engine
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Payloads(Base):
    __tablename__ = "payloads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    input_text: Mapped[str] = mapped_column(String(255), unique=True)
    output_text: Mapped[str] = mapped_column(String(255) )

Base.metadata.create_all(engine)
