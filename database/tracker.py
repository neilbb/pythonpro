from peewee import *

db = SqliteDatabase('tracker.db')


class Entry(Model):


	class Meta:
		database = db





def menu():


#CRUD

def add_entry():
	''' Add entry '''


def view_entry():


def delete_entry(e):


if __name__ == '__main__':
	menu()