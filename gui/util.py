# http://stackoverflow.com/a/16532192/1443496
from tkinter import *
from ttk import * # sudo pip3 install pyttk

import ssa.final as core

root = Tk()
root.title('SSA Graphical Aggregator')
root.geometry('600x400+5+5')
top = Notebook(root, width=1000, height=400)

# we only technically deal with one bundle at a time
bundle = core.Bundle()

import time

class Test:
    count = 0
    def __init__(self):
        self.name = 'test class with str'
        self.n = Test.count
        Test.count += 1
    def __str__(self):
        return '({!s}) {}'.format(self.n, time.asctime())

def bind(widget_dictionary, name, event, func):
    widget_dictionary[name][1].bind(event, func)

# by giving the widget dictionary and the name separately, we can
# defer the evaulation of the listbox control until such a time as it
# is actually created.
def add_new(widget_dictionary, name, cls=Test, bind=None):
    """Adds a new item"""
    def f(entity = None):
        if not entity: entity = cls()
        entity.name = '<name>'
        widget_dictionary[name][1].insert(END, entity.name)
        if bind: bind()
    return f
def del_sel(widget_dictionary, name, bind=None):
    """Deletes the selected item"""
    def f():
        widget_dictionary[name][1].delete(ACTIVE)
        if bind: bind()
    return f
def move(widget_dictionary, lb1, lb2, bind=None):
    """Moves the ACTIVE item from lb1 to lb2

    lb1 and lb2 are names that are in the widget_dictionary
    """
    def f():
        active = widget_dictionary[lb1][1].get(ACTIVE)
        if str(active) != '':   # to avoid moving empty items
            widget_dictionary[lb1][1].delete(ACTIVE)
            widget_dictionary[lb2][1].insert(END, active)
        if bind: bind()
    return f
def new(cls, widget_dictionary, name, **kwargs):
    print('Creating widget {0:<14} under {1}'.format(cls.__name__, name))
    return cls(widget_dictionary[name][1], **kwargs)

# Local Variables:
# truncate-lines: t
# End: