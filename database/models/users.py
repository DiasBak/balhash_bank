# Python
import datetime

# Local
from database.core import Connection
from database.models.cards import Cards
from database.models.accounts import Accounts


class User:
    """Object from db. User."""

    id: int
    first_name: str
    last_name: str
    date_of_birth: datetime.datetime
    iin: str
    phone_number: str

    @staticmethod
    def create(
        conn: Connection,
        first_name: str,
        last_name: str,
        date_of_birth: datetime,
        iin: str,
        phone_number: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO users(
                    first_name,
                    last_name,
                    date_of_birth,
                    iin,
                    phone_number
                )
                VALUES (
                    '{first_name}',
                    '{last_name}',
                    '{date_of_birth}',
                    '{iin}',
                    '{phone_number}'
                )
                """
            )

    # @staticmethod
    # def get(
    #     conn: Connection,
    #     **kwargs: dict[str, any]
    # ) -> 'User':
    #     """SELECT * FROM users WHERE id=1 AND user ='as'"""
    #     condition: list[str] = []
    #     for i in kwargs:
    #         if isinstance(kwargs[i]):
    #             condition.append(f'{i}={kwargs[i]}')
    #     print(' AND '.join(condition))

    #     with conn.cursor() as cur:
    #         cur.execute(
    #             f"""
    #             SELECT * FROM users
    #             WHERE {' AND '.join(condition)}
    #             LIMIT 1
    #             """
    #         )
    #         return cur.fetchone()


    # @staticmethod
    # def all(
    #     conn: Connection,
    # ) -> 'User':
    #     with conn.cursor() as cur:
    #         cur.execute(
    #             f"""
    #             SELECT * FROM users
    #             """
    #         )
    #         return cur.fetchall()
        
    @staticmethod
    def join(
        conn: Connection,
    ) -> 'User':
        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM users
                 
                """
            )
            return cur.fetchone()

                 
        
# User.get(id=123, username='hello')