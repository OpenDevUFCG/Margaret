                            #coding: utf-8
from organization import Organization
import re

class Organization_Controller:

    def __init__(self):
        self.organizations = {}
        self.current_id = 0

    def list_organizations(self):
        return list(self.organizations.values())

    def add_organization(self, name, desc, owner, category):
        
        org_id = self.generate_organization_id()
        organization = Organization(name, desc, owner, category, org_id)
        self.organizations[org_id] = organization
        return org_id

    def remove_organization(self, org_id):
        self.validate_organization_existence(org_id)

        removed_organization = self.organizations[org_id]
        self.organizations.pop(org_id)
        return removed_organization

    def get_organization(self, org_id):
        self.validate_organization_existence(org_id)

        return self.organizations[org_id]

    def modify_organization_by_atribute(self, org_id, atribute, new_atribute_value):
        if not atribute in ['name', 'desc', 'owner', 'category', 'state']:
            raise AttributeError('Atributo Inválido')

        organization = self.organizations[org_id]

        setattr(organization, atribute, new_atribute_value)

    def find_organization_by_atribute(self, atribute, atribute_value):
        if not atribute in ['name', 'category', 'state', 'owner']:
            raise AttributeError('Atributo Inválido')
        
        find_result = []

        for key in self.organizations:
            organization = self.organizations[key]

            organizationAtribute =  getattr(organization, atribute).lower()
            if organizationAtribute == atribute_value.lower() or re.search(atribute_value.lower(), organizationAtribute) != None:
                find_result.append(organization)
            
        return find_result
            
    def generate_organization_id(self):
        self.current_id += 1
        return self.current_id

    def validate_organization_existence(self, org_id):
        if not(org_id in self.organizations):
            raise ValueError('Organização Inexistente')