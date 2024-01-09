from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from res.quotesDb import QuotesDB
from tgbot.config import BOT_TOKEN, DB_PATH

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
db = QuotesDB(dbpath=DB_PATH)

__all__ = ['bot','dp','db']