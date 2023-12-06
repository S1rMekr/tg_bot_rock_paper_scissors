from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


buttons_start: list[KeyboardButton] = [
    KeyboardButton(text='Начать игру'),
    KeyboardButton(text='Закончить игру!')
]

buttons_game: list[KeyboardButton] = [
    KeyboardButton(text='Камень'),
    KeyboardButton(text='Ножницы'),
    KeyboardButton(text='Бумага'),
    KeyboardButton(text='Закончить игру')
]

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[buttons_start],
    resize_keyboard=True
    )

game_keyboard = ReplyKeyboardMarkup(
    keyboard=[buttons_game],
    resize_keyboard=True
)



@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'], 
        reply_markup=start_keyboard
        )
    
@router.message(F.text == 'Начать игру')
async def procces_dog_answer(message:Message):
    await message.answer(
        text='Игра началась! Выберите Камень, Ножницы или Бумагу',
        reply_markup=game_keyboard
    )

@router.message(F.text == 'Закончить игру')
async def procces_cucumber_answer(message:Message):
    await message.answer(
        text='Возвращайтесь, сыграем еще раз!',
    )

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])