# -*- coding: utf-8 -*-

from margaret_back.models.project import Project


class ProjectController:
    def __init__(self):
        self.projects = dict()
        self.current_id = 0

    def add_project(self, name, description, base_text, mentor, mentor_aux,
                    areas):
        project_id = 1
        for _ in self.projects:
            project_id += 1
        self.current_id = project_id

        project = Project(name, description, base_text,
                          mentor, mentor_aux, areas)
                          
        self.projects[project_id] = project
        return project_id

    def list_projects(self):
        return list(self.projects.values())

    def find_projects_by_state(self, state):
        found_projects = {}

        for key, val in self.projects.items():
            if val.state == state:
                found_projects.update({key: val})
        if not found_projects:
            raise Exception('Projects not found!')

        return found_projects

    def find_projects_by_area(self, area):
        found_projects = {}

        for key, val in self.projects.items():
            if area in val.areas:
                found_projects.update({key: val})
        if not found_projects:
            raise Exception('Projects not found!')

        return found_projects

    def update_project_value(self, current_id, key, new_value):
        if current_id in self.projects:
            project = self.projects[current_id]
            if key in project.__dict__:
                setattr(project, key, new_value)
                return project
            else:
                raise AttributeError
        else:
            raise IndexError

    def add_project_area(self, current_id, new_area):
        if current_id in self.projects:
            project = self.projects[current_id]
            project.areas.append(new_area)
            return project
        else:
            raise Exception('Index Error')

    def remove_project_area(self, current_id, area):
        if current_id in self.projects:
            project = self.projects[current_id]
            try:
                project.areas.remove(area)
                return area
            except ValueError as e:
                return e
        else:
            raise IndexError

    def remove_project(self, current_id):
        if current_id in self.projects:
            project = self.projects[current_id]
            del self.projects[current_id]
            return project
        else:
            raise IndexError

    def find_project_by_mentor(self, email_mentor):
        found_projects = {}
        for key, project in self.projects.items():
            if project.check_mentor_by_email(email_mentor):
                found_projects.update({key: project})
        if not found_projects:
            raise Exception('Mentor not found!')

        return found_projects
