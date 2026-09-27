from __future__ import annotations
import json

from .resource import Resource
from .crew_member import CrewMember

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


    def calculer_autonomie_oxygene(self) -> int:
        o2_disponible: int = self.get_ressource("Oxygen").quantite_disponible
        o2_consomme: int = self.calculer_consommation_oxygene_equipage()
        
        if o2_consomme == 0:
            raise ValueError("Impossible de calculer l'autonomie d'oxygene san smembre d'équipage")
        
        return o2_disponible // o2_consomme
    
    
    def to_dict(self) -> dict:
        station: dict = {}
        
        station["name"] = self.name
        station["ressources"] = []
        station["members"] = []
        
        for resource in self.resources.values():
            station["ressources"].append(
                {
                    "nom": resource.nom,
                    "quantite_disponible": resource.quantite_disponible
                }
            )
        
        for member in self.members.values():
            station["members"].append(
                {
                    "nom": member.nom,
                    "role": member.role,
                    "consommation_o2": member.consommation_o2
                }
            )
        
        return station
    
    
    def sauvegarder(self, path: str) -> None:
        if not isinstance(path, str):
            raise TypeError("le chemin de fichier doit être une chaîne de carcatère")
        if not path.strip():
            raise ValueError("le chemin ne peut pas être vide")
        
        data_to_save: dict = self.to_dict()
        
        with open(path, "w", encoding="utf-8") as file:
            json.dump(
                data_to_save,
                file,
                indent=4,
                ensure_ascii=False,
                )
    
    @classmethod
    def charger(cls, path: str) -> Station:
        if not isinstance(path, str):
            raise TypeError("le chemin de fichier doit être une chaîne de carcatère")
        if not path.strip():
            raise ValueError("le chemin ne peut pas être vide")

        
        with open(path, "r", encoding="utf-8") as file:
            data_to_load = json.load(file)
        
        station: Station = cls(data_to_load["name"])
        
        for data_r in data_to_load["ressources"]:
            resource_load: Resource = Resource(data_r["nom"], data_r["quantite_disponible"])
            station.ajouter_ressource(resource_load)
        
        for data_m in data_to_load["members"]:
            member_load: CrewMember = CrewMember(data_m["nom"], data_m["role"], data_m["consommation_o2"])
            station.ajouter_membre(member_load)
        
        return station