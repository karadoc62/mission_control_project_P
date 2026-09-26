import pytest

from src.crew_member import CrewMember


def test_create_member():
    member: CrewMember = CrewMember("Alice", "Commandant", 20)
    
    assert isinstance(member, CrewMember)
    assert member.nom == "Alice"
    assert member.role == "Commandant"
    assert member.consommation_o2 == 20


@pytest.mark.parametrize(
    "name, role, conso",
    [
        (123, "commandant", 20),
        (1.20, "commandant", 20),
        ((1, 2), "commandant", 20),
        ({}, "commandant", 20),
        ([1, 4], "commandant", 20),
        (True, "commandant", 20),
        (None, "commandant", 20),
        
        ("Alice", 123, 20),
        ("Alice", 1.20, 20),
        ("Alice", (1, 2), 20),
        ("Alice", {}, 20),
        ("Alice", [1, 4], 20),
        ("Alice", True, 20),
        ("Alice", None, 20),
        
        ("Alice", "commandant", "test"),
        ("Alice", "commandant", 1.20),
        ("Alice", "commandant", True),
        ("Alice", "commandant", [1, 4]),
        ("Alice", "commandant", (1, 2)),
        ("Alice", "commandant", {}),
        ("Alice", "commandant", None),
    ]
)
def test_crewmember_reject_invalid_type(name, role, conso):
    with pytest.raises(TypeError):
        CrewMember(nom=name, role=role, consommation_o2=conso)


@pytest.mark.parametrize(
    "name, role, conso",
    [
        ("", "commandant", 20),
        ("   ", "commandant", 20),
        
        ("Alice", "", 20),
        ("Alice", "   ", 20),
        
        ("Alice", "commandant", 0),
        ("Alice", "commandant", -10),
    ]
)
def test_crewmember_reject_invalid_value(name, role, conso):
    with pytest.raises(ValueError):
        CrewMember(nom=name, role=role, consommation_o2=conso)


def test_crewmember_repr():
    member_test: CrewMember = CrewMember("Alice", "Commandant", 20)
    
    assert repr(member_test) == "CrewMember(nom='Alice', role='Commandant', consommation_o2=20)"


def test_crewmember_str():
    member_test: CrewMember = CrewMember("Alice", "Commandant", 20)
    
    assert str(member_test) == "Alice - Commandant - 20 unités O2/jour"