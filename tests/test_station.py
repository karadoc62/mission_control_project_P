import json
import pytest

from src.mission_control.crew_member import CrewMember
from src.mission_control.resource import Resource
from src.mission_control.station import Station

# fixture creation
# ----------------

@pytest.fixture
def station():
    return Station("mir")


@pytest.fixture
def oxygen():
    return Resource("Oxygen", 1000)


@pytest.fixture
def alice():
    return CrewMember("Alice", "Commandant", 20)


# tests
# -----
def test_creation_station(station):
    
    assert isinstance(station, Station)
    assert station.name == "mir"
    assert station.resources == {}
    assert station.members == {}


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


def test_station_ajouter_ressource(station, oxygen):
    
    station.ajouter_ressource(resource=oxygen)
    
    assert oxygen.nom in station.resources


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
def test_station_ajouter_ressource_reject_invalid_ressource(invalid_resource, station):
    with pytest.raises(TypeError):
        station.ajouter_ressource(invalid_resource)


def test_station_ajouter_ressource_already_exist(station, oxygen):
    
    station.ajouter_ressource(oxygen)
    with pytest.raises(ValueError):
        station.ajouter_ressource(oxygen)
    assert len(station.resources) == 1


def test_station_get_ressource(station, oxygen):
    station.ajouter_ressource(oxygen)
    
    ressource_get : Resource = station.get_ressource("Oxygen")
    
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
def test_station_get_ressource_reject_invalid_name_type(invalid_name, station):
    with pytest.raises(TypeError):
        station.get_ressource(invalid_name)


@pytest.mark.parametrize(
    "invalid_name",
    [
        "",
        "   ",
    ]
)
def test_station_get_ressource_reject_invalid_name_value(invalid_name,station):
    with pytest.raises(ValueError):
        station.get_ressource(invalid_name)


def test_station_get_ressource_reject_not_exist_ressource(station, oxygen):
    resource_test_2 : Resource = Resource("test_2", 1000)
    
    station.ajouter_ressource(oxygen)
    
    with pytest.raises(KeyError):
        station.get_ressource(resource_test_2.nom)


def test_station_ajouter_membre(station, alice):
    station.ajouter_membre(member=alice)
    
    assert len(station.members) == 1
    assert station.members["Alice"] is alice


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
def test_station_ajouter_membre_reject_invalid_type(invalid_member,station):
    with pytest.raises(TypeError):
        station.ajouter_membre(invalid_member)
    assert not station.members


def test_station_ajouter_membre_reject_member_exist(station, alice):
    station.ajouter_membre(member=alice)
    with pytest.raises(ValueError):
        station.ajouter_membre(member=alice)
    assert len(station.members) == 1
    

def test_station_get_membre(station, alice):
    station.ajouter_membre(member=alice)
    
    member_searched = station.get_membre("Alice")
    assert member_searched is alice
    

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
def test_station_get_membre_invalid_type(invalid_member, station):
    with pytest.raises(TypeError):       
        station.get_membre(invalid_member)
        

@pytest.mark.parametrize(
    "invalid_member",
    [
        "",
        "   ",
    ]
)
def test_station_get_membre_invalid_value(invalid_member, station):
    with pytest.raises(ValueError):       
        station.get_membre(invalid_member)


def test_station_get_membre_reject_inexist_member(station, alice):
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    station.ajouter_membre(member=alice)
    with pytest.raises(KeyError):
        station.get_membre(member_test_2.nom)


def test_station_calculer_consommation_oxygene_equipage(station, alice):
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    member_test_3: CrewMember = CrewMember("Claire", "Officier", 40)
    station.ajouter_membre(member=alice)
    station.ajouter_membre(member=member_test_2)
    station.ajouter_membre(member=member_test_3)
    
    conso_totale: int = station.calculer_consommation_oxygene_equipage()
    
    assert conso_totale == 100
    assert type(conso_totale) is int


def test_station_calculer_consommation_oxygene_equipage_zero_membre(station):
    
    conso_totale: int = station.calculer_consommation_oxygene_equipage()
    
    assert conso_totale == 0
    assert type(conso_totale) is int


def test_station_calculer_autonomie_oxygene(station, oxygen, alice):
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    member_test_3: CrewMember = CrewMember("Claire", "Officier", 40)
    station.ajouter_ressource(oxygen)
    station.ajouter_membre(member=alice)
    station.ajouter_membre(member=member_test_2)
    station.ajouter_membre(member=member_test_3)

    jours_restants: int = station.calculer_autonomie_oxygene()
    assert jours_restants == 10


def test_station_calculer_autonomie_oxygene_with_not_exist_resource(station, alice):
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    member_test_3: CrewMember = CrewMember("Claire", "Officier", 40)
    station.ajouter_membre(member=alice)
    station.ajouter_membre(member=member_test_2)
    station.ajouter_membre(member=member_test_3)

    with pytest.raises(KeyError):
        station.calculer_autonomie_oxygene()


def test_station_calculer_autonomie_oxygene_with_zero_member(station):
    oxygen: Resource = Resource("Oxygen", 1010)
    
    station.ajouter_ressource(oxygen)
    
    with pytest.raises(ValueError):
        station.calculer_autonomie_oxygene()


def test_station_calculer_autonomie_oxygene_with_zero_quantite_dispo(station, alice):
    oxygen: Resource = Resource("Oxygen", 0)
    member_test_2: CrewMember = CrewMember("Paul", "Sous-fifre", 40)
    member_test_3: CrewMember = CrewMember("Claire", "Officier", 40)
    station.ajouter_ressource(oxygen)
    station.ajouter_membre(member=alice)
    station.ajouter_membre(member=member_test_2)
    station.ajouter_membre(member=member_test_3)

    jours_restants: int = station.calculer_autonomie_oxygene()
    assert jours_restants == 0


def test_station_to_dict(station, oxygen, alice):
    water: Resource = Resource("Eau", 5000)
    
    paul: CrewMember = CrewMember("Paul", "Commandant en second", 30)

    station.ajouter_ressource(oxygen)
    station.ajouter_ressource(water)
    
    station.ajouter_membre(alice)
    station.ajouter_membre(paul)
    
    station_data: dict = station.to_dict()

    assert isinstance(station_data, dict)
    assert station_data["name"] == "mir"
    assert isinstance(station_data["ressources"], list)
    assert isinstance(station_data["members"], list)
    
    assert station_data["ressources"][0] == {
            "nom": "Oxygen",
            "quantite_disponible": 1000
        }
    assert station_data["ressources"][1] == {
            "nom": "Eau",
            "quantite_disponible": 5000
        }
    
    assert station_data["members"][0] == {
            "nom": "Alice",
            "role": "Commandant",
            "consommation_o2": 20
        }
    assert station_data["members"][1] == {
            "nom": "Paul",
            "role": "Commandant en second",
            "consommation_o2": 30
        }
    

def test_station_to_dict_empty(station):
    
    station_data: dict = station.to_dict()
    
    assert isinstance(station_data, dict)
    assert station_data["name"] == "mir"
    assert station_data["ressources"] == []
    assert station_data["members"] == []
    

def test_station_sauvegarder(tmp_path, station, oxygen, alice):

    station.ajouter_ressource(oxygen)
    station.ajouter_membre(alice)
    
    fichier = tmp_path / "station_test.json"
    
    station.sauvegarder(str(fichier))
    
    assert fichier.exists()
    
    with open(str(fichier), "r", encoding="utf-8") as file:
        data = json.load(file)

        assert data["name"] == "mir"
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
def test_station_sauvegarder_reject_invalid_type(invalid_path, station):
    
    with pytest.raises(TypeError):
        station.sauvegarder(invalid_path)


@pytest.mark.parametrize(
    "invalid_path",
    [
        "",
        "   ",
    ]
)
def test_station_sauvegarder_reject_invalid_value(invalid_path, station):
                
    with pytest.raises(ValueError):
        station.sauvegarder(invalid_path)


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


def test_station_save_and_load_round_trip(tmp_path, station, oxygen, alice):

    station.ajouter_ressource(oxygen)
    station.ajouter_membre(alice)
    
    fichier = tmp_path / "station_test.json"
    
    station.sauvegarder(str(fichier))
    
    station_loaded: Station = Station.charger(str(fichier))
    
    assert station.name == station_loaded.name
    assert station.resources["Oxygen"].nom == station_loaded.resources["Oxygen"].nom
    assert station.resources["Oxygen"].quantite_disponible == station_loaded.resources["Oxygen"].quantite_disponible
    assert station.members["Alice"].nom == station_loaded.members["Alice"].nom
    assert station.members["Alice"].role == station_loaded.members["Alice"].role
    assert station.members["Alice"].consommation_o2 == station_loaded.members["Alice"].consommation_o2
    
    assert station_loaded is not station
    assert station_loaded.resources["Oxygen"] is not oxygen
    assert station_loaded.members["Alice"] is not alice
    