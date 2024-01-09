import sqlite3
import pytz

from datetime import datetime


class DB:
    def __init__(self, dbpath: str, timezone='UTC'):
        self.dbpath = dbpath
        self.timezone = timezone

    def connect(self) -> sqlite3.Connection:
        con = sqlite3.connect(self.dbpath)
        con.row_factory = self.dictFactory
        return con

    def getCurrentDate(self) -> str:
        return self.getTimezoneDate().strftime('%Y-%m-%d %H:%M:%S')

    def getTimezoneDate(self) -> datetime:
        time = datetime.utcnow()

        utcTz = pytz.timezone('UTC')
        localTz = pytz.timezone(self.timezone)

        utcTime = time.replace(tzinfo=utcTz)
        localTime = utcTime.astimezone(localTz)

        return localTime

    @staticmethod
    def dictFactory(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
        save_dict = {}

        for idx, col in enumerate(cursor.description):
            save_dict[col[0]] = row[idx]

        return save_dict

    @staticmethod
    def updateFormat(sql: str, parameters: dict) -> tuple[str, list]:
        values = ", ".join([
            f"{item} = ?" for item in parameters
        ])
        sql += f" {values}"

        return sql, list(parameters.values())

    @staticmethod
    def updateFormatWhere(sql, parameters: dict) -> tuple[str, list]:
        if not parameters:
            return sql, list()

        sql += " WHERE "

        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])

        return sql, list(parameters.values())
