import pytest

from src.crew_member import CrewMember
from src.resource import Resource
from src.station import Station

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

