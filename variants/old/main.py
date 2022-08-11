import logging
from random import randint

import aiogram.utils.markdown as fmt
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData

import config
import mods

API_TOKEN = config.settings["BOT_TOKEN"]

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

"""
MODS
"""

"""
MODS
"""

"""
https://mastergroosha.github.io/telegram-tutorial-2/buttons/#-
"""

'''
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
'''


@dp.message_handler(commands="special_buttons")
async def cmd_special_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Запросить геолокацию", request_location=True)
    )
    keyboard.add(types.KeyboardButton(text="Запросить контакт", request_contact=True))
    keyboard.add(
        types.KeyboardButton(
            text="Создать викторину",
            request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ),
        )
    )
    await message.answer("Выберите действие:", reply_markup=keyboard)


@dp.message_handler(regexp="(^cat[s]?$|puss)")
async def cats(message: types.Message):
    with open("photos/cat.jpg", "rb") as photo:
        """
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        """
        await message.reply_photo(photo, caption="Cats are here")


@dp.message_handler(regexp="test")
async def test(message: types.Message):
    with open("photos/cat.jpg", "rb") as photo:
        """
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        """
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(
            text="Try", switch_inline_query="Telegram"
        )
        markup.add(switch_button)

        await message.answer_photo(photo, caption="Cats are here")
        await message.answer("Выбрать чат", reply_markup=markup)


""" MENU"""


@dp.message_handler(commands=["start"])
async def menu_start_command(message: types.Message):
    menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_hi = types.KeyboardButton(text="Вызвать меню")
    menu_kb.add(button_hi)

    await message.answer("Добро пожаловать!", reply_markup=menu_kb)


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

    button_inl_site = types.KeyboardButton(
        text="Наш сайт", url="http://craft-projects.com"
    )

    menu_kb_inl.add(button_inl_weather, button_inl_projects)
    menu_kb_inl.add(button_inl_humor, button_inl_random)
    menu_kb_inl.add(button_inl_nasa_apod_photo, button_inl_nasa_epic_photo)
    menu_kb_inl.add(button_inl_site)

    await message.reply("Добро пожаловать в меню!", reply_markup=menu_kb_inl)


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


@dp.callback_query_handler(text="nasa_apod_photo")
async def send_nasa_apod_photo(call: types.CallbackQuery):
    nasa_list = mods.nasa_apod()

    await call.message.answer_photo(nasa_list[0], caption=nasa_list[1])


@dp.callback_query_handler(text="nasa_epic_photo")
async def send_nasa_epic_photo(call: types.CallbackQuery):
    nasa_list = mods.nasa_epic()
    await call.message.answer_photo(nasa_list[0], caption=nasa_list[1])


@dp.callback_query_handler(text="projects_value")
async def send_projects_value(call: types.CallbackQuery):
    await call.message.reply("Тут скоро будут данные о проектах")


@dp.callback_query_handler(text="humor_value")
async def send_humor_value(call: types.CallbackQuery):
    menu_kb_inl = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_inl_random = types.KeyboardButton(text="Ещё", callback_data="humor_value")
    menu_kb_inl.add(button_inl_random)

    await call.message.answer(
        mods.humor(), reply_markup=menu_kb_inl
    )  # +'Тут скоро будут шутки-прибаутки')


"""MENU"""

cb = CallbackData("post", "id", "action")

button = types.InlineKeyboardButton(
    text="Лайкнуть", callback_data=cb.new(id=5, action="like")
)


@dp.callback_query_handler(cb.filter())
async def callbacks(call: types.CallbackQuery, callback_data: dict):
    post_id = callback_data["id"]
    action = callback_data["action"]


@dp.message_handler(lambda message: message.text == "foq_u")
async def foq_u(message: types.Message):
    await message.reply("foq_u!")


""" ECHO """

"""
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
"""

""" ECHO """

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
