# -*- coding: utf-8 -*-

from margaret_back.models.user import User


class Mentor(User):
    def __init__(self, name, email, discord_id, state='', organization=''):
        User.__init__(self, name, email, discord_id)
        self.state = state
