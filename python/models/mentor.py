from user import User


class Mentor(User):
    def __init__(self, name, email, discord_id, state=''):
        User.__init__(self, name, email, discord_id)
        self.__state = state

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
