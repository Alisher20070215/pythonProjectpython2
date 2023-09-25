from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


questions_router = Router()


class UserData(StatesGroup):
    name = State()
    email = State()
    question = State()

@questions_router.message(Command("ask"))
async def start_questions(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    await message.answer("Enter your name")

@questions_router.message(Command("ask"))
async def start_questions(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    await message.answer("Enter your gender")

@questions_router.message(F.text, UserData.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserData.email)
    await message.answer("Enter your e-mail")

@questions_router.message(F.text, UserData.email)
async def process_email(message: Message, state: FSMContext):
    if not "@" in message.text:
        await message.answer("Enter correct e-mail")
    elif " " in message.text.strip():
        await message.answer("Enter correct e-mail")
    else:
        await state.update_data(email=message.text)
        await state.set_state(UserData.question)
        await message.answer("Ask a Question")

@questions_router.message(F.text, UserData.question)
async def process_email(message: Message, state: FSMContext):
    await state.update_data(question=message.text)

@questions_router.message(Command("ask"))
async def start_questions(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    await message.answer("Enter the number of product")

@questions_router.message(F.text, UserData.email)
async def process_email(message: Message, state: FSMContext):
    if "1" in message.text:
        await message.answer("You can buy the book")
    elif "2" in message.text.strip():
        await message.answer("You can buy the clothes")
    elif "3" in message.text.strip():
        await message.answer("You can buy the furniture")
    else:
        await message.answer("Enter number from 1 to 3")

    await message.answer("Thank you, goodbye")
    await state.clear()
