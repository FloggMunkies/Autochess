# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:23:26 2022

@author: mrkno
"""


def print_error(ex):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
