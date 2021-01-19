from margaret_back.models.user import User
from margaret_back.models.subscribed import Subscribed
from pytest import fail

def test_subscribed_create_sucess():
    sub = Subscribed('Midorya', 'deku.arumairo@ccc.ufcg.edu.br', 'Deku#1969', '2016.2', 'LGBTQA+')

    assert sub.name == 'MIDORYA'
    assert sub.email == 'deku.arumairo@ccc.ufcg.edu.br'
    assert sub.discord_id == 'Deku#1969'
    assert sub.period == '2016.2'
    assert sub.minority_group == 'LGBTQA+'

def test_subscribed_null_fields():
    try:
        sub = Subscribed(None,None,None,None)
        fail('Campos Null foram cadastrados')
    except AttributeError:
        pass

def test_sbuscribed_empty_minority_group():
    sub = Subscribed('Todoroki', 'todoroki.shoto@ccc.ufcg.edu.br', 'Shoto#8445', '2015.1', '')
    assert sub.minority_group == ''

def test_subscribed_empty_period():
    try:
        sub = Subscribed('Uraraka', 'uraraka.gravity@ccc.ufcg.edu.br', 'Uravity#4576', '')
        fail('Periodo vazio foi cadastrado')
    except AttributeError:
        pass

def test_subscribed_letters_period():
    try:
        sub = Subscribed('Lida', 'lida.runner@ccc.ufcg.edu.br', 'Runner#4576', 'doismilequize.1')
        fail('Periodo vazio foi cadastrado')
    except AttributeError:
        pass

def test_subscribed_period_without_semester():
    try:
        sub = Subscribed('Bakugo', 'bakugo.numberone@ccc.ufcg.edu.br', 'Boom#4576', '2015')
        fail('Periodo sem semestre foi cadastrado')
    except AttributeError:
        pass


