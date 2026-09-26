class CrewMember:
    
    def __init__(self, nom: str, role: str, consommation_o2: int):
        if not isinstance(nom, str):
            raise TypeError("le nom doit être une chaîne de caractère")
        if not nom.strip():
            raise ValueError("le nom est obligatoire")
        
        if not isinstance(role, str):
            raise TypeError("le role doit être une chaîne de caractère")
        if not role.strip():
            raise ValueError("le role est obligatoire")
        
        if type(consommation_o2) is not int:
            raise TypeError("la consommation d'oxygène doit être un entier")
        if consommation_o2 <= 0:
            raise ValueError("La consommation d'oxygène doit être strictement positive")
        
        self.nom = nom
        self.role = role
        self.consommation_o2 = consommation_o2
