from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание базы данных
engine = create_engine('sqlite:///books.db', echo=True)
Base = declarative_base()

# Создание класса, представляющего таблицу "books"
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

# Создание таблицы
Base.metadata.create_all(engine)

# Функция для добавления новой книги
def add_book(title, author):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_book = Book(title=title, author=author)
    session.add(new_book)
    session.commit()
    session.close()

# Пример использования функции
add_book('Book Title', 'Author Name')