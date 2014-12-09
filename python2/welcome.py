#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import datetime

def greetings():
    print('Welcome to your new Python 2 sandbox.')
    print('Today is {dt:%A} {dt.day} {dt:%B} {dt.year}.'.format(dt=datetime.datetime.now()))


if __name__ == '__main__':
    greetings()
