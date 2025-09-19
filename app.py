import asyncio


from handlers import setup_routers
from loader import dp, bot, db
from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify


async def main():
    setup_routers(dp)
    
    await set_default_commands(bot)
    await on_startup_notify(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
