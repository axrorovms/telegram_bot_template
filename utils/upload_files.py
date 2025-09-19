import os
from aiogram import Bot

from loader import bot


async def save_file(file_id: str, save_dir: str, filename: str) -> str:
    file = await bot.get_file(file_id)

    os.makedirs(save_dir, exist_ok=True)
    full_path = os.path.join(save_dir, filename)

    await bot.download_file(file.file_path, destination=full_path)
    return full_path
