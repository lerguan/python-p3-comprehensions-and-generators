#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n%2 == 0]
    return evens
    pass

def make_exclamation(sentence_list):
    sentence_exclamation= [sentence +'!' for sentence in sentence_list if sentence is not None]
    return sentence_exclamation