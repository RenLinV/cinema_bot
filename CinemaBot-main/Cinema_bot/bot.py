from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

import text
from film_info_processor import film_info
import keyboard as kb

headers = {"X-API-KEY": ""}

bot = Bot(token="")
dp = Dispatcher(storage=MemoryStorage())


class Options(StatesGroup):
    get_by_name = State()
    top_country = State()
    top_genre = State()


@dp.message(Command("start"))
async def second(message: types.Message):
    greeting = text.greeting_builder(message.chat.username, message.chat.first_name)
    await message.answer(greeting)

    await message.answer(
        "{}Выбери, что ты хочешь найти:".format("\U00002753"),
        reply_markup=kb.options_kb.as_markup()
    )


#find movie by its name
@dp.callback_query(lambda c: c.data ==  "name_movies_series")
async def send_name(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введи название фильма или сериала")
    await state.set_state(Options.get_by_name)

@dp.message(Options.get_by_name)
async def find_by_name(message: types.Message, state: FSMContext):
    movie_info, url = film_info.get_by_name(message, headers)
    await bot.send_photo(message.chat.id, photo=url, caption=movie_info)
    await bot.send_message(message.chat.id, text.check_satisfaction)
    await state.clear()


#find top-10 movies in country
@dp.callback_query(lambda c: c.data ==  "countries")
async def send_name(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введи страну")
    await state.set_state(Options.top_country)

@dp.message(Options.top_country)
async def find_by_name(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, 
                           f"{message.text} - чудесная страна, а топ-10 скоро будет, обещаем")
    await bot.send_message(message.chat.id,
                               text.want_another_option)
    await state.clear()


#find top-10 movies in genre
@dp.callback_query(lambda c: c.data ==  "genres")
async def send_name(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введи жанр")
    await state.set_state(Options.top_genre)

@dp.message(Options.top_genre)
async def find_by_name(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, 
                           f"{message.text} - чудесный жанр, а топ-10 скоро будет, обещаем")
    await bot.send_message(message.chat.id,
                               text.want_another_option)
    await state.clear()


#other commands
@dp.message(Command("link"))
async def cmd_link(message):
    await bot.send_message(message.chat.id,
                           "ссылка будет, но мы пока устали🥲")

@dp.message(Command("another"))
async def cmd_another(message, state: FSMContext):
    await message.answer("Введи название фильма или сериала")
    await state.set_state(Options.get_by_name)

@dp.message(Command("restart"))
async def cmd_restart(message):
    await message.answer(
        "{}Выбери, что ты хочешь найти:".format("\U00002753"),
        reply_markup=kb.options_kb.as_markup()
    )

@dp.message(lambda message: message.text[0] == '/')
async def try_wrong_command(message):
    await bot.send_message(message.chat.id, text.cannot_handle)
