from user import User


class Subscribed(User):
    def __init__(self, name, email, discord_id, period='', minority_group=''):
        User.__init__(self, name, email, discord_id)
        self.__period = period
        self.__minority_group = minority_group

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, value):
        return self.__period
