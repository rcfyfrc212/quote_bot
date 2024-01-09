from aiogram.utils.keyboard import InlineKeyboardBuilder

startIkb = InlineKeyboardBuilder()
startIkb.button(text='📥 Добавить цитату', callback_data='add_quote')
startIkb.button(text='📤 Рандомная цитата', callback_data='random_quote')
startIkb = startIkb.as_markup()

cancelIkb = InlineKeyboardBuilder()
cancelIkb.button(text='❌ Отменить', callback_data='cancel')
cancelIkb = cancelIkb.as_markup()