import asyncio
from dotenv import load_dotenv
from os import getenv
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

load_dotenv()
token = getenv("6454319474:AAHXNX7yOeHUuGVhNuFZF7fIliIA1H3xe6o")
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello")

@dp.message(Command("info"))
async def info(message: types.Message):
    print(message.from_user)
    await message.answer(
        f"Привет {message.from_user.first_name}",
    )
