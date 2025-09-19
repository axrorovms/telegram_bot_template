from aiogram import Dispatcher
from . import users, groups, channels, errors

def setup_routers(dp: Dispatcher):
    dp.include_router(users.router)
    dp.include_router(errors.router)
    # dp.include_router(groups.router)
    # dp.include_router(channels.router)
