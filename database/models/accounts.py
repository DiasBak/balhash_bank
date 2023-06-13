# Local
from database.core import Connection
from database.models.users import User

class Accounts:
    id: int
    number: str
    owner_id: User
    balance: str
    type: str

    @staticmethod
    def create(
        conn: Connection,
        number: str,
        owner_id: User,
        balance: str,
        type: str,
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO accounts(
                    number,
                    owner_id,
                    balance,
                    type
                )
                VALUES (
                    '{number}',
                    '{owner_id}',
                    '{balance}',
                    '{type}'
                )
                """
            )
    @staticmethod
    def all(
        conn: Connection,
    ) -> 'Accounts':
        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM accounts
                """
            )
            return cur.fetchall()
        
    @staticmethod
    def join(
        conn: Connection,
    ) -> 'Accounts':
        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM accounts
                INNER JOIN users ON users.id = accounts.owner_id
                """
            )
            return cur.fetchone()