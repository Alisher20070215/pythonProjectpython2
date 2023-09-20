from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

shop_router = Router()

@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Books"),
                KeyboardButton(text="Clothes"),
            ],
            [
                KeyboardButton(text="Furniture"),
            ],
            [KeyboardButton(text="Send contact", request_contact=True)],
            [KeyboardButton(text="Send location", request_location=True)],
            [KeyboardButton(text="Send information", request_information=True)]
        ],
        resize_keyboard=True,
    )
    await message.answer("Select a category below:", reply_markup=kb)


@shop_router.message(F.text == "Books")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("List of books:", reply_markup=kb)
