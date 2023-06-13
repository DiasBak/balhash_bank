#python
from decouple import config
import datetime

#Local
from database.core import Connection
from database.models.users import User
from database.models.cards import Cards
from database.models.accounts import Accounts

my_connecton: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)
if __name__ == '__main__':
    my_connecton.create_tables()

    print(Accounts.join(conn=my_connecton.conn))
    print(User.join(conn=my_connecton.conn))

    # print(Accounts.all(conn=my_connecton.conn))
    # print(Cards.all(conn=my_connecton.conn))

    # User.create(
    #     conn=my_connecton.conn,
    #     first_name='Bob',
    #     last_name='Aiger',
    #     date_of_birth=datetime.datetime(
    #         year=1998,
    #         month=5,
    #         day=15
    #     ),
    #     iin='120516552384',
    #     phone_number='4981560605'
    # )
    
    # Cards.create(
    #     conn=my_connecton.conn,
    #     number='4410415123214567',
    #     cvv='555',
    #     date_end=datetime.datetime(
    #         year=2026,
    #         month=7,
    #         day=1
    #     ),
    #     is_active=True,
    #     pin=9454,
    #     account_id=1
    # )
    # Accounts.create(
    #     conn=my_connecton.conn,
    #     number= '12318273101234567890',
    #     owner_id= 17,
    #     balance='20000',
    #     type='qwer'
    # )