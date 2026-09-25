import pytest

from src.resource import Resource
from src.station import Station

def test_creation_station():
    station_test: Station = Station("mir")
    
    assert isinstance(station_test, Station)
    assert station_test.name == "mir"
    assert station_test.resources == {}


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
    "invaliid_name",
    [
        "",
        "  ",
    ]
)
def test_station_reject_invalid_name_value(invaliid_name):
    with pytest.raises(ValueError):
        Station(invaliid_name)


def test_station_ajouter_ressource():
    station_test : Station = Station("mir")
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
    station_test : Station = Station("mir")
    with pytest.raises(TypeError):
        station_test.ajouter_ressource(invalid_resource)


def test_station_ajouter_ressource_already_exist():
    station_test : Station = Station("mir")
    oxygen : Resource = Resource("Oxygen", 1000)
    
    station_test.ajouter_ressource(oxygen)
    with pytest.raises(ValueError):
        station_test.ajouter_ressource(oxygen)
    assert len(station_test.resources) == 1


def test_station_get_ressource():
    station_test : Station = Station("mir")
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
    station_test : Station = Station("mir")
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
    station_test : Station = Station("mir")
    with pytest.raises(ValueError):
        station_test.get_ressource(invalid_name)


def test_station_get_ressource_reject_not_exist_ressource():
    station_test : Station = Station("mir")
    resource_test : Resource = Resource("test", 1000)
    resource_test_2 : Resource = Resource("test_2", 1000)
    
    station_test.ajouter_ressource(resource_test)
    
    with pytest.raises(KeyError):
        station_test.get_ressource(resource_test_2.nom)