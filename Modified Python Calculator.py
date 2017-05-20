# -*- coding: utf-8 -*-
"""
Created on Sat May 20 12:16:51 2017

@author: EliteBook
"""

# James Gallagher, Studnet Number 10028426
# refactored calculator to handle lists

import math

def add(values):
    # this function will add two numbers
    return (lambda x, y: x+y, values)
    
def subtract(values):
    # this function will subtract two numbers
    return (lambda x, y: x-y, values)

def multiply(values):
    # this function will multiply two numbers
    return (lambda x, y: x-y, values)

def divide(values1, values2):
    # this function will divide two numbers
    if ([v == 0 for v in values2]):
        print "Unable to divide by zero"
    else:
        return map(lambda x, y: x/y, values1, values2)

def minimum(values):
    # this function will find the smallest of a list of number
    return lambda a,b: a if (a>b) else b

def maximum(values):
    # this function will find the biggest of a list of number
    return lambda a,b: a if (a<b) else b

def is_even(values):
    # this function will tell you waht numbers are even in a list of numbers
    return filter(lambda x: x%2 == 0, values)

def is_odd(values):
    # this function will tell you waht numbers are od in a list of numbers 
    return filter(lambda x: x%2 != 0, values)

def is_greater_than(values):
    # this function will tell you which numbers in the list are greater than the mean
    mean = sum(values)/len(values)
    return filter(lambda x: x>mean, values)

def is_less_than(values):
    # this function will tell you which numbers in the list are lesser than the mean
    mean = sum(values)/len(values)
    return filter(lambda x: x<mean, values)

def fahrenheit(temperature):
    # this function converts a temperature to fahrenheit
    return ((float(9)/5)*temperature + 32)

def celsius(temperature):
    # this function converts a temperature to celsius
    return (float(5)/9*(temperature - 32))


    

    

