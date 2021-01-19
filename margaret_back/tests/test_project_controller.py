from margaret_back.controllers.project_controller import ProjectController
from margaret_back.models.mentor import Mentor


def test_id_validation():
    collections = ProjectController()

    collections.add_project('Laguinho', '', '', '', '', ['front'])

    collections.add_project('Roadmap', '', '', '', '', ['documentação'])
    assert collections.current_id == 2

    collections.add_project('Margaret', '', '', '', '', ['refactoring'])
    assert collections.current_id == 3


def test_find_state():
    collections = ProjectController()

    collections.add_project('Margaret', '', '', '', '', [
                            'documentação', 'refactoring'])
    collections.add_project('Roadmap', '', '', '', '', ['design'])
    collections.add_project('Laguinho', '', '', '', '',
                            ['back', 'cloud', 'testes'])
    collections.update_project_value(1, 'state', 'Necessita Revisão')
    projects = collections.find_projects_by_state('Necessita Revisão')

    assert len(list(projects)) == 1


def test_find_area():
    collections = ProjectController()

    collections.add_project('Tamburetei', '', '', '', '', [
                            'front', 'back', 'cloud', 'testes'])
    project = collections.projects[1]

    assert 'front' in project.areas
    assert 'back' in project.areas
    assert 'cloud' in project.areas


def test_update_project_value():
    collections = ProjectController()

    collections.add_project('Horários', '', '', '', '', ['front'])

    collections.update_project_value(1, 'name', 'IssueAi')
    collections.update_project_value(1, 'description', 'Com descrição')
    collections.update_project_value(1, 'base_text', 'Com um texto base')
    project = collections.projects[1]

    assert project.name == 'IssueAi'
    assert project.description == 'Com descrição'
    assert project.base_text == 'Com um texto base'


def test_add_project_area():
    collections = ProjectController()

    collections.add_project('Laguinho', '', '', '', '',
                            ['back', 'cloud', 'testes'])

    collections.add_project_area(1, 'análise de dados')
    project = collections.projects[1]

    assert 'análise de dados' in project.areas


def test_remove_project_area():
    collections = ProjectController()

    collections.add_project('Laguinho', '', '', '', '',
                            ['back', 'cloud', 'testes'])

    collections.remove_project_area(1, 'cloud')
    project = collections.projects[1]

    assert not 'cloud' in project.areas


def test_remove_project():
    collections = ProjectController()

    collections.add_project('Margaret', '', '', '', '',
                            ['back', 'documentação', 'testes'])

    project = collections.remove_project(1)

    assert not collections.projects
    assert project.name == 'Margaret'


def test_find_project_by_mentor():
    collections = ProjectController()

    mentor = Mentor('Juan', 'juan.barros@ccc.ufcg.edu.br',
                    'Juan#3245', '', 'OpenDevUFCG')
    aux_mentor = Mentor(
        'Matheus', 'matheus.alves@ccc.ufcg.edu.br', 'Alves#3245', '', 'OpenDevUFCG')

    collections.add_project('Margaret', '', mentor, aux_mentor,
                            '', ['back', 'documentação', 'testes'])

    assert collections.find_project_by_mentor('juan.barros@ccc.ufcg.edu.br')
    assert collections.find_project_by_mentor('matheus.alves@ccc.ufcg.edu.br')
    try:
        collections.find_project_by_mentor(
            'joao.ribeiro@ccc.ufcg.edu.br')
        fail("Foi encontrado um mentor nao cadastrado")
    except:
        assert True
