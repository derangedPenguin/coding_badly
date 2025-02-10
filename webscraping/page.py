import json

class Page:
    def __init__(self, title:str):
        self.title = title

        self.relations:dict[str, int] = {}
    
    def __str__(self, pretty=False) -> str:
        return json.dumps(self.relations, indent=2 if pretty else None)
    
    def add_relation(self, title:str) -> None:
        '''
        adds :input title: to the relations table, increments by 1 if it already exists in the table
        '''
        self.relations[title] = self.relations.get(title, 0) + 1
    
