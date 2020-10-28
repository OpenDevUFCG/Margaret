# -*- coding: utf-8 -*-
import re

def email_validation(email):
    if isinstance(email, str):
        regex = '^[a-z]+[\._]?[a-z]+[@]{1}[c]{3}[.][c-u]{4}[.][d-u]{3}[.][b-r]{2}$'

        if re.search(regex, email) != None:
            return email

    raise AttributeError('Email inválido!')

def period_validation(period):
    if "." in period:
        periodFormat = period.split(".")
        r = r'^[0-9]{4}$'

        if re.search(r, periodFormat[0]) != None and 2 >= int(periodFormat[1]) > 0:
            return period
    raise AttributeError("Período inválido!")


def empty_validation(value, atributo):
    if value == "":
        raise AttributeError(atributo + " não pode ser vazio!")

def discord_id_validation(value):
    if "#" in value:
        numbers = value.split("#")
        regexNumbers = r'^[0-9]{4}$'

        if  re.search(regexNumbers,numbers[1]) != None:
            return value
        
    raise AttributeError ("Discord inválido!")