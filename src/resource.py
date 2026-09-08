class Resource:
    """Représente une ressource"""
    
    def __init__(self, nom: str, quantite_disponible: int):
        """Initialise une ressource.
        
        Args:
            nom (str): le nom de la ressource
            quantite_disponible (int): la quantité disponible de cette ressource    
        """
        if type(nom) is not str:
            raise TypeError("Le nom de la ressource doit être une chaîne de caractères.")
        if nom.strip() == "":
            raise ValueError("Le nom ne doit pas être vide.")
        
        if type(quantite_disponible) is not int:
            raise TypeError("La quantité disponible doit être une valeur entière.")
        if quantite_disponible < 0:
            raise ValueError("La quantité initiale doit être positive ou nulle.")
        
        self.nom = nom
        self.quantite_disponible = quantite_disponible
    
    
    def consommer(self, value: int) -> None:
        """Retire une quantité à la quantité disponible

        Args:
            value (int): La valeur à ôter de la quantité disponible

        Raises:
            ValueError: si la valeur est négative ou nulle
            ValueError: si la valeur est supérieure à la quantité disponible
            TypeError: si la valeur n'est pas un entier
        """
        if type(value) is not int:
            raise TypeError("La quantité consommée doit être un entier")
        if value <= 0:
            raise ValueError("La quantité consommée doit être strictement positive.")
        if value > self.quantite_disponible:
            raise ValueError("La quantité consommée ne peut être supérieure à la quantité disponible")
        
        self.quantite_disponible -= value
        
        
    def ajouter(self, value: int) -> None:
        """Ajoute une quantité à la quantité disponible

        Args:
            value (int): la quantité à ajouter à la quantité disponible

        Raises:
            ValueError: si la quantité est négative ou nulle
            TypeError: si la quantité n'est pas un entier
        """
        if type(value) is not int:
            raise TypeError("La quantité à ajouter doit être un entier")
        if value <= 0:
            raise ValueError("La quantité à ajouter doit être strictement positive")
        
        self.quantite_disponible += value
        
    
    