#!/usr/bin/env python3 

from collections import OrderedDict
import datetime
import sys

from peewee import *

db = SqliteDatabase('tracker.db')


class Entry(Model):
    content = TextField() #hold any size text
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Entry],safe=True)


def add_entry():
    print("this is add_entry")
    print("Enter entry. Press ctrl+d when finished")
    data = sys.stdin.read().strip() # strip to remove whitespace
    if data:
        if input('Save Entry? [Yn]').lower() !='n':
            Entry.create(content=data)
            print("Saved successfully!")


def view_entry():
    print("this is view_entry")

def delete_entry(e):
    print("this is delete entry")

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entry)
    ])
#the values are function names


def show_menu():
    choice = None
    while choice != 'q':
        print("Enter 'q' to quit.")

        for i,(k,v) in enumerate(menu.items()):
            print("Press {}".format(k))

        choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()


if __name__ == '__main__':
    initialize()
    show_menu()




