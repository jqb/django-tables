# -*- coding: utf-8 -*-

def unique_list(seq):
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked
