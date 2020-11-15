#!/usr/bin/env python
# encoding: utf-8

class BasePlayer(object):

    def __init__(self, name):
        self.name = name
        self.disqualified = False