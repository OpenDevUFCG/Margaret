#coding: utf-8
from python.project import Project

def test_check_email():

    proj = Project("projeto", "", {"email": "mentor@gmail.com"}, "", "", "back")

    assert proj.check_email("mentor@gmail.com")

def test_add_subscriber():

    proj = Project("projeto", "", {"email": "mentor@gmail.com"}, "", "", "back")

    proj.add_subscriber(1, "gabrielly")

    assert proj.get_subscriber(1) == "gabrielly"

    proj.add_subscriber(1, "juan")

    assert proj.get_subscriber(2) == "juan"

    proj.add_subscriber(2, "huandrey")

    assert proj.get_subscriber(3) == "huandrey"

def test_area_setter():

    proj = Project("projeto", "", {"email": "mentor@gmail.com"}, "", "", "back")

    try:
        proj.area = "aleatorio"
        assert False
    except:
        assert True

def test_state_setter():

    proj = Project("projeto", "", {"email": "mentor@gmail.com"}, "", "", "back")

    try:
        proj.state = "aleatorio"
        assert False
    except:
        assert True





    


