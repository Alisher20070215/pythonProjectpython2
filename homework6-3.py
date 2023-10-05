import sqlite3
from pathlib import Path
from pprint import pprint
from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler_router = Router()

@scheduler_router.message(Command("remind"))
async def remind_me(message: types.Message):
    scheduler.add_job(
        send_reminder,
        "date",
        run_date=datetime(2023, 10, 6, 12, 30, 0),
        args=(message.from_user.id,)
    )
    await message.answer("Ok")


async def send_reminder(user_id: int):
    await bot.send_message(user_id, "Hello")


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()
    scheduler = AsyncIOScheduler()


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
        VALUES ('Books'), ('Souvenirs'), ('Manga')
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS questions (
            questionId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            question TEXT,
            userId INTEGER
        )
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
            
        SELECT p.name, c.name FROM product p JOIN category c ON p.categoryId = c.id
        """
    )
    return cursor.fetchall()

def get_product_by_category(category_id: int):
    cursor.execute(
            """
        SELECT * FROM product WHERE categoryId = :c_id
        """,
        {"c_id": category_id},
    )
    return cursor.fetchall()

def get_products_by_category_name(category_name: str):
    cursor.execute(
        """
        SELECT * FROM product WHERE categoryId = (
            SELECT id FROM category WHERE name ILIKE :c_name
        )
        """,
        {"c_name": category_name},
    )
    return cursor.fetchall()

def save_question(data, user_id):
    print(data)
    cursor.execute(
        """
        INSERT INTO questions (name, email, question, userId)
        VALUES (:n, :e, :question, :user_id)
        """,
        {
            "n": data["name"],
            "e": data["email"],
            "question": data["question"],
            "user_id": user_id,
        },
    )
    db.commit()

if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    print(get_product_by_category(1))
