from pydantic import BaseModel
from typing import Optional

class AnimalModel(BaseModel):
        id: Optional[str] = None
        name: str
        age: int
        species: str
        breed: str
        vaccinated: bool
        sex: str
        castrated: bool
        arrival_date: str
        disabled: bool

    # Typisieren
    # Abholung ?
    # def details(self):
    #     return {    "id": self.name,
    #                 "name": self.name,
    #                 "age": self.age,
    #                 "species": self.species,
    #                 "breed": self.breed,
    #                 "vaccinated": self.vaccinated,
    #                 "sex": self.sex,
    #                 "castrated": self.castrated,
    #                 "arrival": self.arrival_date,
    #                 "disabled": self.disabled
    #             }

