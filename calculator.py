#!/usr/bin/env python
# coding: utf-8

# # My First Calculator

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

addition()

subtraction()

multiplication()

division()

modulo()