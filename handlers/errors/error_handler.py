import logging
from aiogram import Router
from aiogram.types import ErrorEvent
from aiogram.exceptions import (
    TelegramBadRequest, TelegramAPIError, TelegramNetworkError,
    TelegramUnauthorizedError, TelegramForbiddenError,
    TelegramEntityTooLarge, TelegramMigrateToChat, TelegramRetryAfter
)

router = Router()


@router.errors()
async def errors_handler(event: ErrorEvent):
    exception = event.exception
    update = event.update

    if isinstance(exception, TelegramUnauthorizedError):
        logging.exception(f"Unauthorized: {exception}")
        return True

    if isinstance(exception, TelegramBadRequest):
        logging.exception(f"BadRequest: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, TelegramForbiddenError):
        logging.exception(f"Forbidden: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, TelegramRetryAfter):
        logging.exception(f"RetryAfter: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, TelegramEntityTooLarge):
        logging.exception(f"EntityTooLarge: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, TelegramMigrateToChat):
        logging.exception(f"MigrateToChat: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f"TelegramAPIError: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, TelegramNetworkError):
        logging.exception(f"TelegramNetworkError: {exception}")
        return True

    # fallback
    logging.exception(f"Unhandled error!\nUpdate: {update}\nException: {exception}")
    return True
