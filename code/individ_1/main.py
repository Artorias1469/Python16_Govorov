#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import greeting_module

greet_template = "Уважаемый %F%, %N%! Вы делаете работу по замыканиям функций."
greet_function = greeting_module.create_greeting(greet_template)

if __name__ == "__main__":
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")

    result = greet_function(last_name, first_name)
    print(result)
