from sqlalchemy import Table, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    books = relationship("Book", backref="author")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    isbn = Column(String(13), unique=True)
    published_date = Column(Date)
    description = Column(String)
    language = Column(String)
    page_count = Column(Integer)
    rating = Column(Numeric(precision=2, scale=1))
    voters = Column(Integer)  # Number of reviewers

    publisher_id = Column(Integer, ForeignKey("publishers.id"))


authors_books_table = Table(
    "authors_books_table",
    Base.metadata,
    Column(Integer, ForeignKey("authors.id")),
    Column(Integer, ForeignKey("books.id")),
)


class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    books = relationship("Book", backref="publisher")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


categories_books_table = Table(
    "categories_books_table",
    Base.metadata,
    Column(Integer, ForeignKey("categories.id")),
    Column(Integer, ForeignKey("books.id")),
)
