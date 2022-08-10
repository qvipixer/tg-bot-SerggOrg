import logging
from aiogram import types
from aiogram.utils.executor import start_webhook
from config import bot, dp, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT


async def on_startup(dispatcher):
    # await database.connect()
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    # await database.disconnect()
    await bot.delete_webhook()


@dp.message_handler()
async def echo(message: types.Message):
    await save(message.from_user.id, message.text)
    messages = await read(message.from_user.id)
    await message.answer(messages)


@dp.message_handler(commands=["start"])
async def menu_start_command(message: types.Message):
    menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_hi = types.KeyboardButton(text="Вызвать меню")
    menu_kb.add(button_hi)

    await message.answer("Добро пожаловать!", reply_markup=menu_kb)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
