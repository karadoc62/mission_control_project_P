from src.mission_control.station import Station

class StationService:
    
    def __init__(self, station: Station):
        if not isinstance(station, Station):
            raise TypeError("L'objet doit être une Station.")
        
        self.station: Station = station
    
    
    def generer_resume(self) -> dict:
        resume: dict = {}
        
        resume['Station'] = self.station.name
        resume['Membres'] = len(self.station.members)
        resume['Ressources'] = len(self.station.resources)
        resume['Consommation O2/jour'] = self.station.calculer_consommation_oxygene_equipage()
        resume['Autonomie O2'] = self.station.calculer_autonomie_oxygene()

        return resume
    
    
    
    
    