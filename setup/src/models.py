"""Models module
module: src/models.py
"""

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    books = relationship("Book", secondary="authors_books_table", backref="authors")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    isbn = Column(String(20), unique=True)
    published_date = Column(Date)
    description = Column(String, default="")
    language = Column(String)
    page_count = Column(Integer, default=1)
    rating = Column(Numeric(precision=2, scale=1), default=0)
    voters = Column(Integer, default=0)  # Number of reviewers

    publisher_id = Column(Integer, ForeignKey("publishers.id"))
    categories = relationship(
        "Category", secondary="categories_books_table", backref="books"
    )


authors_books_table = Table(
    "authors_books_table",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
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
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
)
