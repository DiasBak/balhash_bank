# Python
import datetime

# Local
from database.core import Connection
from database.models.accounts import Accounts


class Cards:
    id: int
    number: str
    cvv: str
    date_end: datetime.datetime
    account_id: Accounts
    is_active: bool
    pin: str

    @staticmethod
    def create(
        conn:Connection,
        number: str,
        cvv: str,
        date_end:datetime.datetime,
        account_id: Accounts,
        is_active: bool,
        pin: str
    ):
        with conn.cursor() as cur:
           cur.execute(f"""
                INSERT INTO cards(
                    number,
                    cvv,
                    date_end,
                    account_id,
                    is_active,
                    pin
                )
                VALUES (
                    '{number}',
                    '{cvv}',
                    '{date_end}',
                    '{account_id}',
                    '{is_active}',
                    '{pin}'
                )
                """
            )
    @staticmethod
    def all(
        conn: Connection,
    ) -> 'Cards':
        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM cards
                """
            )
            return cur.fetchall()