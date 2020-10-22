# -*- coding: utf-8 -*-

from util import validation



class User:
    def __init__(self, name='', email='', discord_id=''):
        self.name = name
        self.email = email
        self.discord_id = discord_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            value = value.upper()
            self._name = value
        else:
            raise Exception('Invalid name!')

    @email.setter
    def email(self,value):
        validation.email_validation(value)
        self.email = value
