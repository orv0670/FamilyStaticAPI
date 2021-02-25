
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._miembros = [
            {
                "id": 0,
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7,13,22]
            },
            {
                "id": 1,
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10,14,3]
            },
            {
                "id": 2,
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def agregar_miembro(self, miembro):
        # fill this method and update the return
        miembro['last_name'] = self.last_name
        self._miembros.append(miembro)
        return self._miembros

    def eliminar_miembro(self, id):
        # fill this method and update the return
        for posicion in range(len(self._miembros)):
            if self._miembros[posicion]['id'] == id:
                self._miembros.pop(posicion)
        return self._miembros
    
    def get_miembro(self, id):
        # fill this method and update the return
        for x in self._miembros:
            if x["id"]== int(id):
                return x

    # this method is done, it returns a list with all the family members
    def get_todos_los_miembros(self):
        return self._miembros
