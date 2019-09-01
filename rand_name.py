#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:13:15 2019

@author: juan
"""


from functools import partial
from itertools import chain, repeat
from random import randint, getrandbits
from unidecode import unidecode

n_min = 1
n_max = 9

get_rand_number=partial(randint, n_min-1, n_max-1)

def repeat_rand_times(char,
                      get_rand_number=get_rand_number,
                      unidecode=unidecode):
    return chain((char,),
                 repeat(unidecode(char), get_rand_number()))

get_coin_toss = partial(getrandbits, 1)

def random_format(txt, whatsapp_formatting_affixes=("_", "*", "~")):
    for afix in whatsapp_formatting_affixes:
        if get_coin_toss():
            txt = txt.join(repeat(afix, 2))
    return txt

def random_case(char):
    if get_coin_toss():
        return char.upper()
    else:
        return char.lower()
#    for afix in whatsapp_formatting_affixes:
#        if get_coin_toss():
#            char = char.join(repeat(afix, 2))
#    return char

def random_name(name="Álvaro"):
    rand_length_map = chain.from_iterable(map(repeat_rand_times, name))
    first_letter = next(rand_length_map)
    rand_case_and_lenght_map = map(random_case, rand_length_map)
    unformatted_rand_name_chain = chain((first_letter,),
                         rand_case_and_lenght_map)
#    formatted_rand_name_map = map(random_format,
#                                  unformatted_rand_name_chain)
    return random_format("".join(unformatted_rand_name_chain))

if __name__ == "__main__":
    for i in range(10):
        print(random_name())
                   