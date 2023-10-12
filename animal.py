class Animal:

    # Details eines Tieres Name, Tierart, Einlieferungsdatum, Alter, Geschlecht, geimpft, kastriert
    def __init__(self,id, name, age, species, breed, vaccinated, sex, castrated, arrival_date, disabled) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.vaccinated = vaccinated
        self.sex = sex
        self.castrated = castrated
        self.arrival_date = arrival_date
        self.disabled = disabled

    # Typisieren
    # Abholung ?
    def details(self):
        return {    "id": self.name,
                    "name": self.name,
                    "age": self.age,
                    "species": self.species,
                    "breed": self.breed,
                    "vaccinated": self.vaccinated,
                    "sex": self.sex,
                    "castrated": self.castrated,
                    "arrival": self.arrival_date,
                    "disabled": self.disabled
                }

