def calculer_autonomie(oxygen_available: int, nb_crew: int, consumption_per_person_per_day: int) -> int:
    """function to determinate how much days the crew can survive in control station

    Args:
        oxygen_available (int): the amount of oxygen available
        nb_crew (int): the number of persons in the crew
        consumption_per_person_per_day (int): the amount of consumed oxygen per person and per day

    Returns:
        int: nb of days available
    """
    # Tests des paramètres
    if type(oxygen_available) is not int:
        raise TypeError("La quantité d'oxygène disponible doit être une valeur entière.")
    elif oxygen_available < 0:
        raise ValueError("La quantité d'oxygène disponible doit être positive ou nulle.")
    
    if type(nb_crew) is not int:
        raise TypeError("Le nombre de personnes dans l'équipage doit être une valeur entière.")
    elif nb_crew <= 0:
        raise ValueError("Le nombre de personnes dans l'équipage doit être une valeur positive.")
    
    if type(consumption_per_person_per_day) is not int:
        raise TypeError("La consommation d'oxygène par personne et par jour doit être une valeur entière.")
    elif consumption_per_person_per_day <= 0:
        raise ValueError("La consommation d'oxygène par personne et par jour doit être une valeur positive.")
        
    daily_consumption: int = nb_crew * consumption_per_person_per_day
    return oxygen_available // daily_consumption