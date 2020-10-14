#coding: utf-8
class Project:
	def __init__(self, name, description, base_text, mentor, aux_mentor, areas):
		self.name = name
		self.description = description
		self.base_text = base_text
		self.project_id = project_id
		self.mentor = "Não confirmado"
		self.aux_mentor = "Não confirmado"
		self.areas = areas
		self.state = "Em análise"
		self.subscribers = {}

	@property
	def areas(self):
		return self.areas
	
	@areas.setter
	def areas(self, areas):
		if not (areas in ['front', 'back', 'cloud', 'testes', 'documentação', 'refactoring', 'design', 'análise de dados', 'scrapping', 'automação', 'bot', 'devops']):
			raise Exception('Área Inválida')
		self.areas = areas

	@property
	def state(self):
		return self.state
		
	@state.setter
    def state(self, state):
        if not (state in ['Em análise', 'Necessita Revisão', 'Pronto - Com sugestões', 'Pronto - Completo']):
            raise Exception('Estado Inválido')
        self._state = state
		
	def add_subscribers(self, key, value):
		self.subscribers[key] = value
	
	def get_subscribers(self, key):
		return self.subscribers[key]