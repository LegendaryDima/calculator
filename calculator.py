#!/usr/bin/env python
# coding: utf-8

# # My First Calculator

calc_on = 1

def addition():
    first = float(input('I will add 2 numbers. What is your first number? '))
    second = float(input('What is your second number? '))
    print(first + second)


def subtraction():
    first = float(input('I will subtract 2 numbers. What is your first number? '))
    second = float(input('What is your second number? '))
    print(first - second)


def multiplication():
    first = float(input('I will muliply 2 numbers. What is your first number? '))
    second = float(input('What is your second number? '))
    print(first * second)


def division():
    first = float(input('I will divide 2 numbers. What is your first number? '))
    second = float(input('What is your second number? '))
    print(first / second)


def modulo():
    first = float(input('I will modulo 2 numbers. What is your first number? '))
    second = float(input('What is your second number? '))
    print(first % second)

def count_to_ten():
    for number in range(1, 11):
        print(number)
    
def quit():
    global calc_on
    calc_on = 0
        
def calc_run():
    op = input('add, subtract, multiply, divide, modulo, ten or quit? ')
    if op == 'add':
        addition()
    elif op == 'subtract':
        subtraction()
    elif op == 'multiply':
        multiplication()
    elif op == 'divide':
        division()
    elif op == 'modulo':
        modulo()
    elif op == 'ten':
        count_to_ten()
    else:
        quit()
        
while calc_on == 1:
    calc_run()