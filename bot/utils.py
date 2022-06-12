import os
import sys
import re
from lxml import html
from pydblite import Base


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def save_in_db(channel, count):
    db = Base(os.path.join(SCRIPT_DIR, f'{channel}_members.db'))
    db.create('members', 'time', mode="open")
    len_db = len(db)
    count_previous = db[len_db - 1]['members'] if len_db else 0
    if count != count_previous:
        db.insert(members=count, time=datetime.datetime.now())
        db.commit()
        return True