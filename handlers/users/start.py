from aiogram import types
from aiogram.filters import CommandStart
from aiogram import Router


router = Router()

# -------------------------------------------------- START --------------------------------------------------------------------
@router.message(CommandStart())
async def bot_start(message: types.Message):
   await message.answer(message.text)

