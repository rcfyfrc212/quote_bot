from random import choice

from .db import DB

class QuotesDB(DB):

    def getQuotesCount(self) -> int:
        with self.connect() as con:
            return con.execute(
                'SELECT COUNT(*) FROM quotes'
            ).fetchone()['COUNT(*)']
    
    def getRandomQuote(self) -> str:
        with self.connect() as con:
            quotes = con.execute(
                'SELECT * FROM quotes'
            ).fetchall()

            return choice(quotes)['quote']

    def addQuote(self, quote: str):
        with self.connect() as con:
            con.execute(f'INSERT INTO quotes (quote) VALUES (?)',[quote])
