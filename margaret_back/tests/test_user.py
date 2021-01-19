# -*- coding: utf-8 -*-
from margaret_back.models.user import User
from pytest import fail

def test_user_nome():
    user = User("Vladimir Lenin", "lenin.vladimir@ccc.ufcg.edu.br","lenin#0803")
    assert user.name == "VLADIMIR LENIN"
    assert user.email == "lenin.vladimir@ccc.ufcg.edu.br"
    assert user.discord_id == "lenin#0803"

def test_user_null_fields():
    try:
        user = User(None,None,None)
        fail()
    except AttributeError:
        pass

def test_user_name_empty():
    try:
        user = User("", "lenin.vladimir@ccc.ufcg.edu.br","lenin#0803")
        fail()
    except AttributeError:
        pass

def test_user_email_empty():
    try:
        user = User("Vladimir Lenin", "","lenin#0803")
        fail()
    except AttributeError:
        pass

def test_user_discord_empty():
    try:
        user = User("Vladimir Lenin", "lenin.vladimir@ccc.ufcg.edu.br","")
        fail()
    except AttributeError:
        pass

def test_user_name_not_string():
    try:
        user = User(1917, "lenin.vladimir@ccc.ufcg.edu.br","lenin#0803")
        fail()
    except AttributeError:
        pass

def test_user_discord_wrong_format():
    
    try:
        user = User("Vladimir Lenin", "lenin.vladimir@ccc.ufcg.edu.br","lenin#803")
        fail()
    except AttributeError:
        pass

    try:
        user = User("Vladimir Lenin", "lenin.vladimir@ccc.ufcg.edu.br","lenin0803")
        fail()
    except AttributeError:
        pass

    try:
        user = User("Vladimir Lenin", "lenin.vladimir@ccc.ufcg.edu.br","lenin#lenin")
        fail()
    except AttributeError:
        pass


def test_user_email_wrong_format():
    try:
        user = User("Vladimir Lenin", "lenin.vladimir@gmail.com","lenin#0803")
        fail()          
    except AttributeError:        
        pass
        
    try:
        user = User("Vladimir Lenin", "lenin.vladimirccc.ufcg.edu.br","lenin#0803") 
        fail()
    except AttributeError:        
        pass    

    try:
        user = User("Vladimir Lenin", "lenin.vladimir@ufcg.edu.br","lenin#0803")
        fail()            
    except AttributeError:        
        pass

    

    