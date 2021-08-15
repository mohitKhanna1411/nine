from peewee import SqliteDatabase, Model, TextField, IntegerField, AutoField, DateTimeField, BlobField, ForeignKeyField
import os
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
DB_NAME = os.environ.get("DB_NAME")
db = SqliteDatabase(DB_NAME)

# basetable


class BaseTable(Model):
    class Meta:
        database = db

# Users inheriting basetable
# Users table defination


class Users(BaseTable):
    id = AutoField()
    uuid = TextField(null=False)
    created_at = DateTimeField(default=datetime.now())
    username = TextField(null=False, unique=True)
    password = TextField(null=False)

# Articles table defination
# Articles inheriting basetable


class Articles(BaseTable):
    id = AutoField()
    uuid = TextField(null=False)
    user_id = ForeignKeyField(Users, backref='articles')
    title = TextField()
    body = TextField()
    date = TextField()


# TagNames table defination
# TagNames inheriting basetable


class TagNames(BaseTable):
    id = AutoField()
    name = TextField(null=False, unique=True)


# Tags table defination
# Tags inheriting basetable


class Tags(BaseTable):
    id = AutoField()
    tag_id = ForeignKeyField(TagNames, backref='tags')
    article_id = ForeignKeyField(Articles, backref='tags')


def create_db():
    # check for file
    if os.path.exists(DB_NAME):
        print("Database already exists.", flush=True)
        return False
    # creating the tables
    db.connect()
    db.create_tables([Users, Articles, TagNames, Tags])
