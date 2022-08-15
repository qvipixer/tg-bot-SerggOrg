import logging
from random import randint

import aiogram.utils.markdown as fmt
from aiogram import types
from aiogram.utils.executor import start_webhook

import db
import mods
from config import bot, dp, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT


async def on_startup(dispatcher):
    # await database.connect()
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    # await conn.close()
    await bot.delete_webhook()


"""
''' ECHO '''
@dp.message_handler()
async def echo(message: types.Message):
    await db.save(message.from_user.id, message.text)
    # await message.answer(message.text + " Твой ИД " + str(message.from_user.id))
''' ECHO '''
"""

""" CAT """


@dp.message_handler(regexp="(^cat[s]?$|puss)")
async def cats(message: types.Message):
    with open("photos/cat.jpg", "rb") as photo:
        await message.reply_photo(photo, caption="Коцык тута")
        await db.save(message.from_user.id, message.text)


@dp.message_handler(regexp="test")
async def test(message: types.Message):
    with open("photos/cat.jpg", "rb") as photo:
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(
            text="Try", switch_inline_query="Telegram"
        )
        markup.add(switch_button)

        await db.save(message.from_user.id, message.text)
        await message.answer_photo(photo, caption="Коцык тута")
        await message.answer("Выбрать чат", reply_markup=markup)


""" CAT """

""" MENU"""


@dp.message_handler(lambda message: message.text == "Вызвать меню")
async def without_puree(message: types.Message):
    menu_kb_inl = types.InlineKeyboardMarkup(resize_keyboard=True)

    button_inl_weather = types.KeyboardButton(
        text="Погода", callback_data="weather_value"
    )
    button_inl_projects = types.KeyboardButton(
        text="Проекты", callback_data="projects_value"
    )
    button_inl_humor = types.KeyboardButton(text="Шутки", callback_data="humor_value")
    button_inl_random = types.KeyboardButton(
        text="Рандом", callback_data="random_value"
    )
    button_inl_nasa_apod_photo = types.KeyboardButton(
        text="NASA APOD", callback_data="nasa_apod_photo"
    )
    button_inl_nasa_epic_photo = types.KeyboardButton(
        text="NASA EPIC", callback_data="nasa_epic_photo"
    )

    button_inl_random_cat = types.KeyboardButton(
        text="Коцыки", callback_data="random_cat"
    )

    menu_kb_inl.add(button_inl_weather, button_inl_projects)
    menu_kb_inl.add(button_inl_humor, button_inl_random)
    menu_kb_inl.add(button_inl_nasa_apod_photo, button_inl_nasa_epic_photo)
    menu_kb_inl.add(button_inl_random_cat)

    await message.reply("Добро пожаловать в меню!", reply_markup=menu_kb_inl)


""" CMD """


@dp.message_handler(commands=["start"])
async def menu_start_command(message: types.Message):
    menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_hi = types.KeyboardButton(text="Вызвать меню")
    menu_kb.add(button_hi)
    await db.save(message.from_user.id, message.text)
    await message.answer(
        "Добро пожаловать!" "Поддержать разработчика" "https://sobe.ru/na/S2X2E0W8g1Z5",
        reply_markup=menu_kb,
    )


@dp.message_handler(commands=["db_drop"])
async def menu_start_command(message: types.Message):
    await db.db_drop()
    await message.reply("db_drop")


@dp.message_handler(commands=["db_add"])
async def menu_start_command(message: types.Message):
    await db.db_add()
    await message.reply("db_add")


""" DONATE """


@dp.message_handler(commands=["donate"])
async def menu_start_command(message: types.Message):
    # menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # button_donate = types.KeyboardButton(text="Поддержать разработчика")
    # menu_kb.add(button_donate)
    await db.save(message.from_user.id, message.text)
    await message.answer(
        "Поддержать разработчика" "https://sobe.ru/na/S2X2E0W8g1Z5"
    )  # , reply_markup=menu_kb)


""" DONATE """

""" CMD """

""" TEXT """


@dp.callback_query_handler(text="weather_value")
async def send_weather_value(call: types.CallbackQuery):
    weather_list = mods.weather()

    await call.message.answer(
        fmt.text(
            fmt.text("Погода в Жлобине"),
            fmt.text("Вчера в это время: " + weather_list[0]),
            fmt.text("Сейчас: " + weather_list[1]),
            fmt.text("Ощущается как : " + weather_list[2]),
            fmt.text("Ветер: " + weather_list[3]),
            fmt.text("Влажность: " + weather_list[4]),
            fmt.text("Давление: " + weather_list[5]),
            fmt.text("Световой день: " + weather_list[6]),
            fmt.text(weather_list[7]),
            fmt.text(weather_list[8]),
            fmt.text(weather_list[9]),
            sep="\n",
        ),
        parse_mode="HTML",
    )
    # await call.message.reply('Тут скоро будут погодные данные')


@dp.callback_query_handler(text="random_cat")
async def send_random_cat(call: types.CallbackQuery):
    menu_kb_inl = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_inl_random_cat = types.KeyboardButton(
        text="Ещё кота?", callback_data="random_cat"
    )
    menu_kb_inl.add(button_inl_random_cat)
    await call.message.answer_photo(mods.random_cat(), reply_markup=menu_kb_inl)


@dp.callback_query_handler(text="nasa_apod_photo")
async def send_nasa_apod_photo(call: types.CallbackQuery):
    nasa_list = mods.nasa_apod()
    await call.message.answer_photo(nasa_list[0], caption=nasa_list[1])


@dp.callback_query_handler(text="nasa_epic_photo")
async def send_nasa_epic_photo(call: types.CallbackQuery):
    nasa_list = mods.nasa_epic()
    await call.message.answer_photo(nasa_list[0], caption=nasa_list[1])


@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    menu_kb_inl = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_inl_random = types.KeyboardButton(
        text="Сыграем?", callback_data="random_value"
    )
    menu_kb_inl.add(button_inl_random)

    await call.message.answer(
        ("Число от 0 до 10 было :  " + str(randint(0, 10))), reply_markup=menu_kb_inl
    )


@dp.callback_query_handler(text="humor_value")
async def send_humor_value(call: types.CallbackQuery):
    menu_kb_inl = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_inl_humor = types.KeyboardButton(text="Ещё", callback_data="humor_value")
    menu_kb_inl.add(button_inl_humor)

    await call.message.answer(mods.humor(), reply_markup=menu_kb_inl)


@dp.callback_query_handler(text="projects_value")
async def send_projects_value(call: types.CallbackQuery):
    await call.message.reply("Тут скоро будут данные о проектах")


""" TEXT """

"""MENU"""

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
