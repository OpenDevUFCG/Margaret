# -*- coding: utf-8 -*-
from margaret_back.models.mentor import Mentor


class MentorController:
    def __init__(self):
        self.mentors = {}

    def add_mentor(self, name, email, discord, state):
        self.validating_existing_email(email)
        mentor = Mentor(name, email, discord, state)
        self.mentors[email] = mentor
        return self.mentors[email]

    def list_mentor(self):
        return self.mentors.values()

    def find_mentors_by_attribute(self, attribute, value_attribute):
        if attribute.lower() not in ['name', 'email', 'discord', 'state', 'organization']:
            raise AttributeError("Atributo inválido")
        
        found_mentors = []
        
        for mentor in self.mentors.values():
            if value_attribute.lower() in getattr(mentor, attribute):
                found_mentors.append(mentor)
        return found_mentors

    def modify_mentor_by_attribute(self, email_user, attribute, new_attribute):
        if attribute.lower() not in ['name', 'email', 'discord', 'state', 'organization']:
            raise AttributeError("Atributo inválido")
        
        self.validate_mentor_existence(email_user)
        setattr(self.mentors[email_user], attribute, new_attribute)

    def remove_mentor(self, email_user):
        self.validate_mentor_existence(email_user)
        del self.mentors[email_user]

    def validate_mentor_existence(self, email_user):
        if not email_user in self.mentors.keys():
            raise ValueError("Usuário não inscrito")

    def validating_existing_email(self, email):
        if email in self.mentors.keys():
            raise ValueError("Email já em uso")
