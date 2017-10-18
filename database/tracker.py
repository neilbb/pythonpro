from peewee import *
import datetime

db = SqliteDatabase('tracker.db')


class Entry(Model):
	content = TextField() #hold any size text
	timestamp = DateTimeField(default=datatime.datatime.now)

	class Meta:
		database = db


def initialize():
	db.connect()
	db.create_tables([Entry],safe=True)


def menu():


#CRUD

def add_entry():
	''' Add entry '''


def view_entry():


def delete_entry(e):


if __name__ == '__main__':
	initialize()
	menu()