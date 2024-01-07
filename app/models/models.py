from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.database import Base


class Headers(Base):
    __tablename__ = "headers"

    header_id = Column(Integer, primary_key=True)
    name = Column(String)
    sales_rep_id = Column(Integer, ForeignKey('salesrep.sales_rep_id'))
    buyer_id = Column(Integer, ForeignKey('buyers.buyer_id'))
    active = Column(String)
    buyers: Mapped["Buyers"] = relationship(back_populates="headers", uselist=False)
    sales_rep:  Mapped["SalesRep"] = relationship(back_populates="headers", uselist=False)
    lines:  Mapped["Lines"] = relationship(back_populates="headers", uselist=False)


class Lines(Base):
    __tablename__ = "lines"

    line_id = Column(Integer, primary_key=True)
    header_id = Column(Integer, ForeignKey('headers.header_id'))
    name = Column(String)
    market_id = Column(Integer, ForeignKey('markets.market_id'))
    item_id = Column(Integer, ForeignKey('items.item_id'))
    creation_date = Column(String)
    headers: Mapped["Headers"] = relationship(back_populates="lines", uselist=False)
    markets: Mapped["Markets"] = relationship(back_populates="lines", uselist=False)
    items: Mapped["Items"] = relationship(back_populates="lines", uselist=False)


class Buyers(Base):
    __tablename__ = "buyers"

    buyer_id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String)
    headers: Mapped["Headers"] = relationship(back_populates="buyers", uselist=False)


class Items(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    lines: Mapped["Lines"] = relationship(back_populates="items", uselist=False)


class Markets(Base):
    __tablename__ = "markets"

    market_id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    lines: Mapped["Lines"] = relationship(back_populates="markets", uselist=False)


class Resource(Base):
    __tablename__ = "resource"

    resource_id = Column(Integer, primary_key=True)
    name = Column(String)
    sales_rep: Mapped["SalesRep"] = relationship(back_populates="resource", uselist=False)


class SalesRep(Base):
    __tablename__ = "salesrep"

    sales_rep_id = Column(Integer, primary_key=True)
    resource_id = Column(Integer, ForeignKey('resource.resource_id'))
    headers: Mapped["Headers"] = relationship(back_populates="sales_rep", uselist=False)
    resource: Mapped["Resource"] = relationship(back_populates="sales_rep", uselist=False)
