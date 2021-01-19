# -*- coding: utf-8 -*-
from margaret_back.models.subscribed import Subscribed

class SubscribedsController:

    def __init__(self):
        self.subscribers = {}       

    def add_subscriber(self,name,email,discord,period,minoritary_group):
        self.validating_existing_email(email)
        subscribed = Subscribed(name,email,discord,period,minoritary_group)       
        self.subscribers[email] = subscribed
        return self.subscribers[email]

    def list_subscribeds(self):
        return list(self.subscribers.values())

    def find_subscribed_by_attribute(self,attribute,value_attribute):
        if attribute.lower() not in['name','email','discord_id','period','minoritary_group']:
            raise AttributeError("Atributo inválido")

        found_subscribers = []
        
        for sub in self.subscribers.values():        
            print(sub.discord_id)

            if value_attribute.upper() in getattr(sub,attribute).upper():
                found_subscribers.append(sub)
            
           
            

        return found_subscribers


    def modify_subscribed_by_attribute(self,email_user,attribute,new_attribute):
        if attribute.lower() not in['name','email','discord_id','period','minoritary_group']:
            raise AttributeError("Atributo inválido")
        
        if attribute.lower() == "email":
            raise AttributeError("Impossível alterar e-mail")

        modified_sub = self.get_subscribed(email_user)        
       
        setattr(modified_sub,attribute,new_attribute)
        
    def get_subscribed(self,email_user):
        if not email_user in self.subscribers.keys():   
            raise ValueError("Usuário não inscrito")

        return self.subscribers[email_user]


    def remove_subscribed(self,email_user):       
        removed_subs = self.get_subscribed(email_user)    
        
        self.subscribers.pop(email_user)
        return removed_subs              

            
    def validating_existing_email(self,email):
        if email in self.subscribers.keys():
            raise ValueError("Email já em uso")    
    
    