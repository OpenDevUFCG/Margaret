# -*- coding: utf-8 -*-

from margaret_back.models.user import User
from margaret_back.util import validation
import json

class Subscribed(User):
    def __init__(self, name, email, discord_id, period, minority_group=''):
        User.__init__(self, name, email, discord_id)
        self.period = period
        self.minority_group = minority_group
    
    @property
    def period(self):
        return self._period
    
    @period.setter
    def period(self, value):
        validation.period_validation(value)
        self._period = value

    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

