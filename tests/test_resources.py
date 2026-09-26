import pytest
from src.mission_control.resources import calculer_autonomie

def test_calculer_autonomie_avec_reste():
    result = calculer_autonomie(1000, 5, 30) # 1000 // (5 * 30)
    assert result == 6
    

def test_nb_jours_exact():
    result = calculer_autonomie(1000, 5, 50)
    assert result == 4


def test_pas_assez_de_jours():
    result = calculer_autonomie(100, 5, 50)
    assert result == 0


def test_pas_assez_de_jours_pour_journee_sup_complete():
    result = calculer_autonomie(251, 5, 50)
    assert result == 1


def test_un_seul_mb_equipage():
    result = calculer_autonomie(250, 1, 50)
    assert result == 5
    

# Tests sur oxygene disponible
def test_oxygene_disponible_negatif():
    with pytest.raises(ValueError):
        calculer_autonomie(-100, 5, 50)


def test_oxygene_disponible_nul():
    result = calculer_autonomie(0, 5, 50)
    assert result == 0


def test_oxygene_disponible_float():
    with pytest.raises(TypeError):
        calculer_autonomie(12.5, 5, 50)


def test_oxygene_disponible_non_entier():
    with pytest.raises(TypeError):
        calculer_autonomie("test", 5, 50)
        
        
# Tests sur nb membres equipages
def test_nb_equipage_negatif():
    with pytest.raises(ValueError):
        calculer_autonomie(1000, -1, 50)


def test_nb_equipage_nul():
    with pytest.raises(ValueError):
        calculer_autonomie(1000, 0, 50)


def test_nb_equipage_float():
    with pytest.raises(TypeError):
        calculer_autonomie(1000, 2.5, 50)


def test_nb_equipage_non_entier():
    with pytest.raises(TypeError):
        calculer_autonomie(1000, "Test", 50)


# Tests sur consommation
def test_conso_quotidienne_negative():
    with pytest.raises(ValueError):
        calculer_autonomie(1000, 4, -10)
        

def test_conso_quotidienne_nulle():
    with pytest.raises(ValueError):
        calculer_autonomie(1000, 4, 0)


def test_conso_quotidienne_float():
    with pytest.raises(TypeError):
        calculer_autonomie(1000, 4, 50.5)


def test_conso_quotidienne_non_entier():
    with pytest.raises(TypeError):
        calculer_autonomie(1000, 4, "test")


# bool interdit sur les 3 paramètres
@pytest.mark.parametrize(
    "oxygen_available, nb_crew, consumption_per_person_per_day",
    [
        (True, 5, 50),
        (1000, True, 50),
        (1000, 5, True),
    ]
)
def test_bool_interdit(oxygen_available, nb_crew, consumption_per_person_per_day):
    with pytest.raises(TypeError):
        calculer_autonomie(oxygen_available, nb_crew, consumption_per_person_per_day)