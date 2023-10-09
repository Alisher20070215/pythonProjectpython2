from aiogram import types, Router, F

admin_router = Router()

FORBIDDEN_WORDS = ["hello", "fool"]


@admin_router.message(Command(["ban"], prefix='/!'))
async def ban_user(message: types.Message):
    author = message.reply_to_message.from_user.id
    print(message.reply_to_message.from_user.id)
    await bot.ban_chat_member(message.chat.id, author)


@admin_router.message(Command(["pin"], prefix='/!'))
async def ban_user(message: types.Message):
    await bot.ban_chat_member(message.chat.id, message.message_id)


@admin_router.message(F.chat.type != 'private')
async def catch_words(message: types.Message):
    for w in FORBIDDEN_WORDS:
        if w in message.text.lower():
            await message.answer("You can't use words like that")
            await message.delete()
            break
