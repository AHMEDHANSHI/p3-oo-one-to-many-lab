class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self,name, pet_type,owner=None) -> None:
        self.name=name
        self.pet_type=pet_type
        if pet_type  not  in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type")
        self.owner=owner
        Pet.all.append(self)
    
    

class Owner:
    def __init__(self,name) -> None:
        self.name=name
        pass
    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]
    # returns all pets that belong to this owner {self }
    def add_pet(self,pet):
        pet.owner=self
        return pet
    def get_sorted_pets(self):
        return sorted(self.pets(),key=lambda pet: pet.name)
        
        
    