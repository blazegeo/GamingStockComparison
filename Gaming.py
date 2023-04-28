#!/usr/bin/env python
# coding: utf-8

# In[5]:



def sony_pte(price: float):
    """ For conversion of price to price-to-earning ratio for Sony using 2022 earning per share"""
    ratio = price / 6.28
    return "%.2f" %ratio

def ea_pte(price: float):
    """ For conversion of price to price to earning ratio for Electronic Arts using 2022 earning per share"""
    ratio = price / 2.76
    return "%.2f" %ratio

def blizzard_pte(price: float):
    """ For conversion of price to price-to-earning ratio for Activision Blizzard using 2022 earning per share"""
    ratio = price / 1.92
    return "%.2f" %ratio

def nintendo_pte(price: float):
    """ For conversion of price to price-to-earning ratio for Nintendo using 2022 earning per share"""
    ratio = price / 0.90
    return "%.2f" %ratio

def enix_pte(price: float):
    """ For conversion of price to price-to-earning ratio for Square Enix using 2022 earning per share"""
    ratio = price / 0.90
    return "%.2f" %ratio

