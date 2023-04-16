# create class pets
class Pets:
    # class variables
    #name = "Sally"
    #age = 6

    def __init__(self, name, age):
        #print("this is the constructor method for class Pets")
        self.name = name
        self.age = age

    def setSurname (self, last_name):
        self.name += ' ' + last_name
        
    def getSurname(self):
        return self.name


pet1 = Pets('Anna', 99)
pet2 = Pets('Sally', 1)
pet3 = Pets('Suuri', 2)
petsList = [pet1, pet2, pet3]
surname = 'Slita'
for pet in petsList:
    print(pet.name,'\nAdding surname...')
    pet.setSurname(surname)
    print('Full name is - ', pet.getSurname())

