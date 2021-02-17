# -*- coding: utf-8 -*-

from margaret_back.util import validation
from flask_restx import fields, Model

user_schema = Model('User', {
    'owner': fields.String,
    'email': fields.String,
    'discord_id': fields.String,
})


class User:
    def __init__(self, name, email, discord_id):
        self.name = name
        self.email = email
        self.discord_id = discord_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):

            validation.empty_validation(value, 'Nome')
            value = value.upper()
            self._name = value
        else:
            raise AttributeError('Nome inválido')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        validation.email_validation(value)
        self._email = value

    @property
    def discord_id(self):
        return self._discord_id

    @discord_id.setter
    def discord_id(self, value):
        if isinstance(value, str):
            validation.empty_validation(value, 'Discord ID')
            validation.discord_id_validation(value)
            self._discord_id = value
