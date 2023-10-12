from animal import Animal
animals: list[Animal] = []
@app.get("/animals")
def get_animals():
    return [Animal.name, Animal.species, Animal.arrival_date]