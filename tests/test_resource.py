import pytest

from src.resource import Resource

def test_creation_resource():
    oxygen = Resource("Oxygène", 1000)
    assert isinstance(oxygen, Resource)
    assert oxygen.nom == "Oxygène"
    assert oxygen.quantite_disponible == 1000


@pytest.mark.parametrize(
    "name, amount",
    [
        (123, 1000),
        ("test", "test"),
        ("test", True)
    ]
)
def test_resource_bad_type(name, amount):
    with pytest.raises(TypeError):
        Resource(name, amount)


@pytest.mark.parametrize(
    "name, amount",
    [
        ("   ", 1000),
        ("test", -100),
    ]
)
def test_resource_bad_value(name, amount):
    with pytest.raises(ValueError):
        Resource(name, amount)


def test_add_amount():
    oxygen = Resource("Oxygene", 1000)
    oxygen.ajouter(100)
    assert oxygen.quantite_disponible == 1100


@pytest.mark.parametrize(
    "value",
    [
        True,
        "test"
    ]
)
def test_add_amount_must_be_int(value):
    oxygen = Resource("oxygen", 1000)
    with pytest.raises(TypeError):
        oxygen.ajouter(value)
    assert oxygen.quantite_disponible == 1000


def test_add_amount_negative_value():
    oxygen = Resource("oxygen", 1000)
    with pytest.raises(ValueError):
        oxygen.ajouter(-100)
    assert oxygen.quantite_disponible == 1000
        
        
def test_add_amount_zero_value():
    oxygen = Resource("oxygen", 1000)
    with pytest.raises(ValueError):
        oxygen.ajouter(0)
    assert oxygen.quantite_disponible == 1000


def test_subtract_amount():
    oxygen = Resource("oxygen", 1000)
    oxygen.consommer(100)
    assert oxygen.quantite_disponible == 900


@pytest.mark.parametrize(
    "value",
    [
        "test",
        True,
    ]
)
def test_subtract_amount_must_be_int(value):
    oxygen = Resource("oxygen", 1000)
    with pytest.raises(TypeError):
        oxygen.consommer(value)
    assert oxygen.quantite_disponible == 1000


@pytest.mark.parametrize(
    "value",
    [
        0,
        -100,
        10000
    ]
)
def test_subtract_amount_bad_value(value):
    oxygen = Resource("oxygen", 1000)
    with pytest.raises(ValueError):
        oxygen.consommer(value)
    assert oxygen.quantite_disponible == 1000


