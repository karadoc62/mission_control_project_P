from src.mission_control.station import Station
from src.mission_control.resource import Resource
from src.mission_control.crew_member import CrewMember


if __name__ == "__main__" :
    
    station_mir: Station = Station("Mir")
    
    oxygen: Resource = Resource("Oxygène", 1000)
    water: Resource = Resource("Eau", 5000)
    
    alice: CrewMember = CrewMember("Alice", "Commandant", 30)
    paul: CrewMember = CrewMember("Paul", "Commandant en second", 30)
    claire: CrewMember = CrewMember("Claire", "Technicienne en ingénierie aérospatiale", 20)
    karadoc: CrewMember = CrewMember("Karadoc", "Passager clandestin", 25)
    
    station_mir.ajouter_ressource(oxygen)
    station_mir.ajouter_ressource(water)
    
    station_mir.ajouter_membre(alice)
    station_mir.ajouter_membre(paul)
    station_mir.ajouter_membre(claire)
    station_mir.ajouter_membre(karadoc)
    
    # station_mir.sauvegarder("station.json")
    # print(str(oxygen))
    
    # # au bout de deux jours:
    # oxygen.consommer((station_mir.calculer_consommation_oxygene_equipage()) * 2)
    
    # station_mir.sauvegarder("station.json")
    # print(str(oxygen))
    
    station_chargee: Station = Station.charger("station.json")
    
    print(station_chargee.name)
    print(station_chargee.resources)
    print(station_chargee.members)