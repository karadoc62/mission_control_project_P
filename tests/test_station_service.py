from src.mission_control.services.station_service import StationService
from src.mission_control.station import Station
from src.mission_control.resource import Resource
from src.mission_control.crew_member import CrewMember


import pytest

@pytest.fixture
def station_mir():
    station_mir: Station = Station("Mir")
    
    oxygen: Resource = Resource("Oxygen", 1000)
    water: Resource = Resource("Water", 5000)
    
    alice: CrewMember = CrewMember("Alice", "Commandant", 30)
    paul: CrewMember = CrewMember("Paul", "Pilote", 30)
    zergei: CrewMember = CrewMember("Zergei", "Copilote", 30)
    
    station_mir.ajouter_ressource(oxygen)
    station_mir.ajouter_ressource(water)
    station_mir.ajouter_membre(alice)
    station_mir.ajouter_membre(paul)
    station_mir.ajouter_membre(zergei)

    return station_mir


@pytest.fixture
def station_service_test(station_mir):
    station_service_test: StationService = StationService(station_mir)
    return station_service_test



@pytest.mark.parametrize(
    "invalid_station",
    [
        "",
        "   ",
        123,
        True,
        (1, 2),
        {},
        12.1
    ]
)
def test_station_service_reject_invalid_station(invalid_station):
    with pytest.raises(TypeError):
        StationService(invalid_station)


def test_station_service_create_stationService(station_service_test):
    assert isinstance(station_service_test, StationService)


def test_station_service_generer_resume_create_dict(station_service_test):
    assert isinstance(station_service_test.generer_resume(), dict)


def test_station_service_nb_resources_is_valid(station_service_test):
    resume: dict = station_service_test.generer_resume()
    assert resume['Ressources'] == 2


def test_station_service_nb_member_is_valid(station_service_test):
    resume: dict = station_service_test.generer_resume()
    assert resume['Membres'] == 3


def test_station_service_name_is_valid(station_service_test):
    resume: dict = station_service_test.generer_resume()
    assert resume['Station'] == "Mir"

    
def test_station_service_conso_is_valid(station_service_test):
    resume: dict = station_service_test.generer_resume()
    assert resume['Consommation O2/jour'] == 90


def test_station_service_autonomie_is_valid(station_service_test):
    resume: dict = station_service_test.generer_resume()
    assert resume['Autonomie O2'] == 11  # 1000 // 90
    

def test_station_service_is_station_instance(station_service_test, station_mir):
    assert station_service_test.station is station_mir


def test_station_service_reject_missing_resources():
    station_mir: Station = Station("Mir")
    station_service_test: StationService = StationService(station_mir)
    
    with pytest.raises(KeyError):
        station_service_test.generer_resume()

    
def test_station_service_reject_missing_members():
    station_mir: Station = Station("Mir")
    oxygen: Resource = Resource("Oxygen", 1000)
    station_mir.ajouter_ressource(oxygen)
    station_service_test: StationService = StationService(station_mir)
    
    with pytest.raises(ValueError):
        station_service_test.generer_resume()