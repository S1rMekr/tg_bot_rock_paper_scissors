from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import game_kb, start_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'], 
        reply_markup=start_kb
        )

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=start_kb)

@router.message(F.text == LEXICON_RU['yes_button'])
async def procces_yes_answer(message:Message):
    await message.answer(
        text=LEXICON_RU['yes'],
        reply_markup=game_kb
    )

@router.message(F.text == LEXICON_RU['no_button'])
async def procces_no_answer(message:Message):
    await message.answer(
        text=LEXICON_RU['no']
    )

@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]}'
                         f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner],
                         reply_markup=start_kb)