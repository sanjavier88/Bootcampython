import datetime
from peewee import *
from decouple import config

db = MySQLDatabase(
    'lista_contactos',
    host=(config('MYSQL_HOST')),
    user='root',
    password=(config('MYSQL_PASSWORD')),
    port=int(config('MYSQL_PORT'))
)


class User(Model):  # tablas
    email = TextField()
    password = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'users'

    @classmethod
    def create_user(cls, email, password):
        return User.create(email=email, password=password)


class Contacts(Model):  # tablas
    phone = TextField()
    cell_phone = TextField()
    user = ForeignKeyField(User, backref='contacts')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'contacts'


db.create_tables([User, Contacts])
