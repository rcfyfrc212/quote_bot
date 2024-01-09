import os
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from aiogram.fsm.context import FSMContext

from .loader import dp, db
from .keyboards import startIkb, cancelIkb
from .states import States

@dp.message(CommandStart())
async def start(message: Message):
    try:
        await message.answer(
            text='Добро пожаловать! 👋\n'
                f'Количество цитат в боте: <code>{db.getQuotesCount()}</code>\n',
            reply_markup=startIkb
        )
    
    except:
        await message.answer('❌ Ошибка, попробуйте позже')

@dp.callback_query(F.data == 'add_quote')
async def addQuote(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text='Введите цитату: ',
        reply_markup=cancelIkb
    )

    await state.set_state(States.addQuote)

@dp.message(States.addQuote)
async def addQuoteHandler(message: Message, state: FSMContext):
    quote = message.text

    if len(quote) < 10:
        return await message.answer(
            text='❗️ Минимальная длина цитаты 10 символов!\nВведите цитату:',
            reply_markup=cancelIkb
        )
    
    try:
        db.addQuote(quote)
        await message.answer('✅ Новая цитата добавлена! Главное меню - /start')
    
    except:
        await message.answer('❌ Не удалось добавить новую цитату! Главное меню - /start')

@dp.callback_query(F.data == 'random_quote')
async def randomQuote(callback: CallbackQuery):
    try:
        if db.getQuotesCount():
            await callback.message.answer(
                "<b>Рандомная цитата: </b>\n"
                f"<code>{db.getRandomQuote()}</code>\n\n"
                "Главное меню - /start"
            )
        
        else:
            await callback.message.answer('❗️ В базе еще ни одной цитаты! Главное меню - /start')
    
    except:
        await callback.message.answer(
            '❌ Невозможно получить рандомную цитату\n Главное меню - /start'
        )

@dp.callback_query(F.data == 'cancel')
async def cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer('❌ Действие отменено')
    await callback.message.delete()

@dp.message()
async def unknown(message: Message):
    await message.answer('Главное меню - /start')