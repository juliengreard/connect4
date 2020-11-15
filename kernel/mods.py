#!/usr/bin/env python
# encoding: utf-8

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

Players = enum("Manual", "Bot")
