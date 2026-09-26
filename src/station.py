from src.resource import Resource
from src.crew_member import CrewMember

class Station:
    
    def __init__(self, name: str):
        
        if not isinstance(name, str):
            raise TypeError("le nom de la station doit être une chaîne de caractère")
        elif not name.strip():
            raise ValueError("Le nom de la station est obligatoire")
        
        self.name: str = name
        self.resources: dict[str, Resource] = {}
        self.members: dict[str, CrewMember] = {}
        
    
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
    
    
    def ajouter_membre(self, member: CrewMember) -> None:
        if not isinstance(member, CrewMember):
            raise TypeError("le membre ajouté doit être de type CrewMember")
        if member.nom in self.members:
            raise ValueError("le membre est déjà présent dans l'équipage")

        self.members[member.nom] = member
    
    
    def get_membre(self, member_name: str) -> CrewMember:
        if not isinstance(member_name, str):
            raise TypeError("le nom du membre recherché doit être une chaîne de caractères")
        if not member_name.strip():
            raise ValueError("Le nom du membre d'équipage est obligatoire")
        
        if member_name not in self.members:
            raise KeyError("le membre recherché n'existe pas")
        
        return self.members[member_name]


    def calculer_consommation_oxygene_equipage(self) -> int:
        conso_globale: int = 0
        
        for member in self.members.values():
            conso_globale += member.consommation_o2
        
        return conso_globale