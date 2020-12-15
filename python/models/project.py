# coding: utf-8

class Project:
    def __init__(self, name, description, mentor, aux_mentor, base_text, areas):
        self.name = name
        self.description = description
        self.base_text = base_text
        self.mentor = mentor
        self.aux_mentor = aux_mentor
        self.areas = areas
        self.state = "Em análise"
        self.subscribers = {}

    @property
    def areas(self):
        return self._areas

    @areas.setter
    def areas(self, areas):
        # Modificar depois
        for area in areas:
            area = area.lower()
            if area in ['front', 'back', 'cloud', 'testes', 'documentação', 'refactoring', 'design', 'análise de dados', 'scrapping', 'automação', 'bot', 'devops']:
                self._areas = areas
            else:
                raise Exception('Área Inválida')

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        state = state.title()
        if not (state in ['Em Análise', 'Necessita Revisão', 'Pronto - Com Sugestões', 'Pronto - Completo']):
            raise Exception('Estado Inválido')
        self._state = state

    def add_subscriber(self, key, value):
        if key not in self.subscribers:
            self.subscribers[key] = value
        else:
            key += 1
            self.subscribers[key] = value

    def get_subscriber(self, key):
        return self.subscribers[key]

    def check_email(self, email):
        mentor = self.mentor
        return email == mentor["email"]

    def check_mentor_by_email(self, email):
        return self.mentor.email == email or self.aux_mentor.email == email
