#!/usr/bin/env python3 

from peewee import *
import datetime

db = SqliteDatabase('tracker.db')


class Entry(Model):
    content = TextField() #hold any size text
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db



def initialize():
    db.connect()
    db.create_tables([Entry],safe=True)

def menu():
    '''test'''

def add_entry():
    '''test'''

def view_entry():
    '''test'''

def delete_entry(e):
    '''test'''

if __name__ == '__main__':
    initialize()
    menu()