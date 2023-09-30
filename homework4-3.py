import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()

def create_tables():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS questions (
            questionId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price FLOAT,
            picture TEXT,
        """
    )
    def populate_tables():
        cursor.execute(
            """
        INSERT INTO category (name)
        VALUES ('Books'), ('Clothes'), ('Furniture')
        """
    )
    cursor.execute(
        """
        INSERT INTO product (name, price, picture, categoryId)
        VALUES ('Anna Karenina', 2000.0, '/images/book.jpg', 1),
        ('War and Peace', 3000.0, '/images/book.jpg', 1),
        ('Children's bookends', 200.0, '/images/book.jpg', 2),
        ('Attack on Titan', 3000.0, '/images/book.jpg', 3)
        """
    )
    db.commit()

    def get_products():
        cursor.execute(
            """
            SELECT * FROM product
            SELECT p.name, c.name FROM product p JOIN category c ON p.categoryId = c.id
            """
        )
        return cursor.fetchall()

    def get_product_by_category(category_id):
        cursor.execute(
            """
            SELECT * FROM product WHERE categoryId = :c_id
            """,
            {"c_id": category_id},
        )
        return cursor.fetchall()

    if __name__ == "__main__":
        init_db()
        create_tables()
        populate_tables()
        print(get_product_by_category(1))
