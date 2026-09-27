import json
import pytest

from src.mission_control.crew_member import CrewMember
from src.mission_control.resource import Resource
from src.mission_control.station import Station

def test_creation_station():
    station_test: Station = Station("mir")
    
    assert isinstance(station_test, Station)
    assert station_test.name == "mir"
    assert station_test.resources == {}
    assert station_test.members == {}


@pytest.mark.parametrize(
    "invalid_name",
    [
        123,
        False,
        None,
        (1, 2),
        {}
    ]
)
def test_station_reject_invalid_name_type(invalid_name):
    with pytest.raises(TypeError):
        Station(invalid_name)


@pytest.mark.parametrize(
    "invalid_name",
    [
        "",
        "  ",
    ]
)
def test_station_reject_invalid_name_value(invalid_name):
    with pytest.raises(ValueError):
        Station(invalid_name)


def test_station_ajouter_ressource():
    station_test: Station = Station("mir")
    oxygen : Resource = Resource("Oxygen", 1000)
    
    station_test.ajouter_ressource(resource=oxygen)
    
    assert oxygen.nom in station_test.resources


@pytest.mark.parametrize(
    "invalid_resource",
    [
        123,
        "test",
        False,
        None,
        (1, 2),
        {}
    ]
)
def test_station_ajouter_ressource_reject_invalid_ressource(invalid_resource):
    station_test: Station = Station("mir")
    with pytest.raises(TypeError):
        station_test.ajouter_ressource(invalid_resource)


def test_station_ajouter_ressource_already_exist():
    station_test: Station = Station("mir")
    oxygen : Resource = Resource("Oxygen", 1000)
    
    station_test.ajouter_ressource(oxygen)
    with pytest.raises(ValueError):
        station_test.ajouter_ressource(oxygen)
    assert len(station_test.resources) == 1


def test_station_get_ressource():
    station_test: Station = Station("mir")
    oxygen : Resource = Resource("Oxygen", 1000)
    station_test.ajouter_ressource(oxygen)
    
    ressource_get : Resource = station_test.get_ressource("Oxygen")
    
    assert isinstance(ressource_get, Resource)
    assert ressource_get.nom == "Oxygen"
    assert ressource_get.quantite_disponible == 1000
    assert ressource_get is oxygen
    

@pytest.mark.parametrize(
    "invalid_name",
    [
        123,
        False,
        None,
        (1, 2),
        {}
    ]
)
def test_station_get_ressource_reject_invalid_name_type(invalid_name):
    station_test: Station = Station("mir")
    with pytest.raises(TypeError):
        station_test.get_ressource(invalid_name)


@pytest.mark.parametrize(
    "invalid_name",
    [
        "",
        "   ",
    ]
)
def test_station_get_ressource_reject_invalid_name_value(invalid_name):
    station_test: Station = Station("mir")
    with pytest.raises(ValueError):
        station_test.get_ressource(invalid_name)


def test_station_get_ressource_reject_not_exist_ressource():
    station_test: Station = Station("mir")
    resource_test: Resource = Resource("test", 1000)
    resource_test_2 : Resource = Resource("test_2", 1000)
    
    station_test.ajouter_ressource(resource_test)
    
    with pytest.raises(KeyError):
        station_test.get_ressource(resource_test_2.nom)


def test_station_ajouter_membre():
    station_test: Station = Station("mir")
    member_test: CrewMember = CrewMember("Alice", "Commandant", 20)
    station_test.ajouter_membre(member=member_test)
    
    assert len(station_test.members) == 1
    assert station_test.members["Alice"] is member_test


@pytest.mark.parametrize(
    "invalid_member",
    [
        123,
        1.20,
        True,
        (1, 2),
        {},
        "test",
        None,
    ]
)
def test_station_ajouter_membre_reject_invalid_type(invalid_member):
    station_test: Station = Station("mir")
    with pytest.raises(TypeError):
        station_test.ajouter_membre(invalid_member)
    assert not station_test.members


def test_station_ajouter_membre_reject_member_exist():
    station_test: Station = Station("mir")
    member_test: CrewMember = CrewMember("Alice", "Commandant", 20)
    station_test.ajouter_membre(member=member_test)
    with pytest.raises(ValueError):
        station_test.ajouter_membre(member=member_test)
    assert len(station_test.members) == 1
    

def test_station_get_membre():
    station_test: Station = Station("mir")
    member_test: CrewMember = CrewMember("Alice", "Commandant", 20)
    station_test.ajouter_membre(member=member_test)
    
    member_searched = station_test.get_membre("Alice")
    assert member_searched is member_test
    

@pytest.mark.parametrize(
    "invalid_member",
    [
        123,
        1.20,
        True,
        (1, 2),
        {},
        None,
    ]
)
def test_station_get_membre_invalid_type(invalid_member):
    station_test: Station = Station("mir")
    with pytest.raises(TypeError):       
        station_test.get_membre(invalid_member)
        

@pytest.mark.parametrize(
    "invalid_member",
    [
        "",
        "   ",
    ]
)
def test_station_get_membre_invalid_value(invalid_member):
    station_test: Station = Station("mir")
    with pytest.raises(ValueError):       
        station_test.get_membre(invalid_member)


def test_station_get_membre_reject_inexist_member():
    station_test: Station = Station("mir")
    member_test_1: CrewMember = CrewMember("Alice", "Commandant", 20)
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    station_test.ajouter_membre(member=member_test_1)
    with pytest.raises(KeyError):
        station_test.get_membre(member_test_2.nom)


def test_station_calculer_consommation_oxygene_equipage():
    station_test: Station = Station("mir")
    member_test_1: CrewMember = CrewMember("Alice", "Commandant", 20)
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    member_test_3: CrewMember = CrewMember("Claire", "Officier", 40)
    station_test.ajouter_membre(member=member_test_1)
    station_test.ajouter_membre(member=member_test_2)
    station_test.ajouter_membre(member=member_test_3)
    
    conso_totale: int = station_test.calculer_consommation_oxygene_equipage()
    
    assert conso_totale == 100
    assert type(conso_totale) is int


def test_station_calculer_consommation_oxygene_equipage_zero_membre():
    station_test: Station = Station("mir")
    
    conso_totale: int = station_test.calculer_consommation_oxygene_equipage()
    
    assert conso_totale == 0
    assert type(conso_totale) is int


def test_station_calculer_autonomie_oxygene():
    station_test: Station = Station("mir")
    oxygen: Resource = Resource("Oxygen", 1010)
    member_test_1: CrewMember = CrewMember("Alice", "Commandant", 20)
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    member_test_3: CrewMember = CrewMember("Claire", "Officier", 40)
    station_test.ajouter_ressource(oxygen)
    station_test.ajouter_membre(member=member_test_1)
    station_test.ajouter_membre(member=member_test_2)
    station_test.ajouter_membre(member=member_test_3)

    jours_restants: int = station_test.calculer_autonomie_oxygene()
    assert jours_restants == 10


def test_station_calculer_autonomie_oxygene_with_not_exist_resource():
    station_test: Station = Station("mir")
    member_test_1: CrewMember = CrewMember("Alice", "Commandant", 20)
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    member_test_3: CrewMember = CrewMember("Claire", "Officier", 40)
    station_test.ajouter_membre(member=member_test_1)
    station_test.ajouter_membre(member=member_test_2)
    station_test.ajouter_membre(member=member_test_3)

    with pytest.raises(KeyError):
        station_test.calculer_autonomie_oxygene()


def test_station_calculer_autonomie_oxygene_with_zero_member():
    station_test: Station = Station("mir")
    oxygen: Resource = Resource("Oxygen", 1010)
    
    station_test.ajouter_ressource(oxygen)
    
    with pytest.raises(ValueError):
        station_test.calculer_autonomie_oxygene()


def test_station_calculer_autonomie_oxygene_with_zero_quantite_dispo():
    station_test: Station = Station("mir")
    oxygen: Resource = Resource("Oxygen", 0)
    member_test_1: CrewMember = CrewMember("Alice", "Commandant", 20)
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    member_test_3: CrewMember = CrewMember("Claire", "Officier", 40)
    station_test.ajouter_ressource(oxygen)
    station_test.ajouter_membre(member=member_test_1)
    station_test.ajouter_membre(member=member_test_2)
    station_test.ajouter_membre(member=member_test_3)

    jours_restants: int = station_test.calculer_autonomie_oxygene()
    assert jours_restants == 0


def test_station_to_dict():
    station_mir: Station = Station("Mir")
        
    oxygen: Resource = Resource("Oxygène", 1000)
    water: Resource = Resource("Eau", 5000)
    
    alice: CrewMember = CrewMember("Alice", "Commandant", 30)
    paul: CrewMember = CrewMember("Paul", "Commandant en second", 30)


    station_mir.ajouter_ressource(oxygen)
    station_mir.ajouter_ressource(water)
    
    station_mir.ajouter_membre(alice)
    station_mir.ajouter_membre(paul)
    
    station_data: dict = station_mir.to_dict()

    assert isinstance(station_data, dict)
    assert station_data["name"] == "Mir"
    assert isinstance(station_data["ressources"], list)
    assert isinstance(station_data["members"], list)
    
    assert station_data["ressources"][0] == {
            "nom": "Oxygène",
            "quantite_disponible": 1000
        }
    assert station_data["ressources"][1] == {
            "nom": "Eau",
            "quantite_disponible": 5000
        }
    
    assert station_data["members"][0] == {
            "nom": "Alice",
            "role": "Commandant",
            "consommation_o2": 30
        }
    assert station_data["members"][1] == {
            "nom": "Paul",
            "role": "Commandant en second",
            "consommation_o2": 30
        }
    

def test_station_to_dict_empty():
    station_test: Station = Station("Mir")
    
    station_data: dict = station_test.to_dict()
    
    assert isinstance(station_data, dict)
    assert station_data["name"] == "Mir"
    assert station_data["ressources"] == []
    assert station_data["members"] == []
    

def test_station_sauvegarder(tmp_path):
    station_mir: Station = Station("Mir")
            
    oxygen: Resource = Resource("Oxygène", 1000)
    
    alice: CrewMember = CrewMember("Alice", "Commandant", 30)

    station_mir.ajouter_ressource(oxygen)
    station_mir.ajouter_membre(alice)
    
    fichier = tmp_path / "station_test.json"
    
    station_mir.sauvegarder(str(fichier))
    
    assert fichier.exists()
    
    with open(str(fichier), "r", encoding="utf-8") as file:
        data = json.load(file)

        assert data["name"] == "Mir"
        assert isinstance(data["ressources"], list)
        assert isinstance(data["members"], list)
        assert data["ressources"]
        assert data["members"]
    

@pytest.mark.parametrize(
    "invalid_path",
    [
        123,
        1.20,
        True,
        (1, 2),
        {},
        None,
    ]
)
def test_station_sauvegarder_reject_invalid_type(invalid_path):
    station_mir: Station = Station("Mir")
    
    with pytest.raises(TypeError):
        station_mir.sauvegarder(invalid_path)


@pytest.mark.parametrize(
    "invalid_path",
    [
        "",
        "   ",
    ]
)
def test_station_sauvegarder_reject_invalid_value(invalid_path):
    station_mir: Station = Station("Mir")
                
    with pytest.raises(ValueError):
        station_mir.sauvegarder(invalid_path)


def test_station_charger(tmp_path):
    
    fichier = tmp_path / "station_test.json"
    
    # contenu du fichier json qui sera chargé
    data_to_save: dict = {
        "name": "Mir",
        "ressources": [
            {
                "nom": "Oxygène",
                "quantite_disponible": 1000
            }
        ],
        "members": [
            {
                "nom": "Alice",
                "role": "Commandant",
                "consommation_o2": 30
            },
            {
                "nom": "Paul",
                "role": "Commandant en second",
                "consommation_o2": 30
            }
        ]
    }
    
    # Création du fichier json
    with open(fichier, "w", encoding="utf-8") as file:
        json.dump(
            data_to_save,
            file,
            indent=4,
            ensure_ascii=False,
        )
    
    station_loaded: Station = Station.charger(str(fichier))
    
    assert isinstance(station_loaded, Station)
    assert station_loaded.name == "Mir"
    
    for res in station_loaded.resources.values():
        assert isinstance(res, Resource)

    assert station_loaded.resources["Oxygène"].nom == "Oxygène"
    assert station_loaded.resources["Oxygène"].quantite_disponible == 1000
        
    for mem in station_loaded.members.values():
        assert isinstance(mem, CrewMember)
    
    assert station_loaded.members["Alice"].nom == "Alice"
    assert station_loaded.members["Alice"].role == "Commandant"
    assert station_loaded.members["Alice"].consommation_o2 == 30
    
    assert station_loaded.members["Paul"].nom == "Paul"
    assert station_loaded.members["Paul"].role == "Commandant en second"
    assert station_loaded.members["Paul"].consommation_o2 == 30


@pytest.mark.parametrize(
    "invalid_path",
    [
        123,
        1.20,
        True,
        (1, 2),
        {},
        None,
    ]
)
def test_station_charger_invalid_type(invalid_path):
    
    with pytest.raises(TypeError):
        Station.charger(invalid_path)


@pytest.mark.parametrize(
    "invalid_path",
    [
        "",
        "   ",
    ]
)
def test_station_charger_invalid_value(invalid_path):
    
    with pytest.raises(ValueError):
        Station.charger(invalid_path)


def test_station_save_and_load_round_trip(tmp_path):
    station_mir: Station = Station("Mir")
                
    oxygen: Resource = Resource("Oxygène", 1000)
    
    alice: CrewMember = CrewMember("Alice", "Commandant", 30)

    station_mir.ajouter_ressource(oxygen)
    station_mir.ajouter_membre(alice)
    
    fichier = tmp_path / "station_test.json"
    
    station_mir.sauvegarder(str(fichier))
    
    station_loaded: Station = Station.charger(str(fichier))
    
    assert station_mir.name == station_loaded.name
    assert station_mir.resources["Oxygène"].nom == station_loaded.resources["Oxygène"].nom
    assert station_mir.resources["Oxygène"].quantite_disponible == station_loaded.resources["Oxygène"].quantite_disponible
    assert station_mir.members["Alice"].nom == station_loaded.members["Alice"].nom
    assert station_mir.members["Alice"].role == station_loaded.members["Alice"].role
    assert station_mir.members["Alice"].consommation_o2 == station_loaded.members["Alice"].consommation_o2
    
    assert station_loaded is not station_mir
    assert station_loaded.resources["Oxygène"] is not oxygen
    assert station_loaded.members["Alice"] is not alice
    