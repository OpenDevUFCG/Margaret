# -*- coding: utf-8 -*-

from margaret_back.models.user import User
from flask_restx import fields, Model


mentor_schema = Model('MentorList', {
    "name": fields.String,
    "email": fields.String,
    "discord_id": fields.String,
    "state": fields.String,
})

class Mentor(User):
    def __init__(self, name, email, discord_id, state='', organization=''):
        User.__init__(self, name, email, discord_id)
        self.state = state
