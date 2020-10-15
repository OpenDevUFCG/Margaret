import re
from error import *


class User:
    def __init__(self, name='', email='', discord_id=''):
        self.name = name
        self.__email = email
        self.__discord_id = discord_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = value.upper()
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def discord_id(self):
        return self.__discord_id

    @discord_id.setter
    def discod_id(self, value):
        return self.__discord_id

    def email_validacion(self):
        regex = '^[a-z]+[\._]?[a-z]+[@]{1}[c]{3}[.][c-u]{4}[.][d-u]{3}[.][b-r]{2}$'
        try:
            if re.search(regex, self.__email):
                email_error()
        except EmailError as error:
            print(error)