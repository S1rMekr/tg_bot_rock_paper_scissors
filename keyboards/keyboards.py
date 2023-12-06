from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])


start_kb_builder = ReplyKeyboardBuilder()

start_kb_builder.row(button_yes, button_no, width=2)

start_kb: ReplyKeyboardMarkup = start_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

buttons_game: list[KeyboardButton] = [
    KeyboardButton(text='Камень'),
    KeyboardButton(text='Ножницы'),
    KeyboardButton(text='Бумага'),
]

game_kb = ReplyKeyboardMarkup(
    keyboard=[buttons_game],
    resize_keyboard=True
)