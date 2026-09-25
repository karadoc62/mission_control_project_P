from src.resource import Resource

class Station:
    
    def __init__(self, name: str):
        
        if not isinstance(name, str):
            raise TypeError("le nom de la station doit être une chaîne de caractère")
        elif not name.strip():
            raise ValueError("Le nom de la station est obligatoire")
        
        self.name: str = name
        self.resources: dict[str, Resource] = {}
        
    
    def ajouter_ressource(self, resource: Resource) -> None:
        
        if not isinstance(resource, Resource):
            raise TypeError("La valeur renseignée doit être de la classe Resource.")
        if resource.nom in self.resources:
            raise ValueError("La ressource existe déjà")
        
        self.resources[resource.nom] = resource
        
    
    def get_ressource(self, resource_name: str) -> Resource:
        
        if not isinstance(resource_name, str):
            raise TypeError("le nom de la ressource doit être une chaine de caractere")
        elif not resource_name.strip():
            raise ValueError("le nom de la ressource est obligaotire")
        elif not resource_name in self.resources:
            raise KeyError("la ressource demandée n'existe pas")
        
        return self.resources[resource_name]
    
    
        
        