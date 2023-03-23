# Jorge Andres Gandara Oliveros T00065470
class Object:
    def __init__(self,id = int, cost_per_weigth = float, description = str, provider = str) -> None:
        self._id=id
        self._cost_per_weigth=cost_per_weigth
        self._description=description
        self._provider=provider
class Package:
    def __init__(self, id = int, objects = [Object], weight = 0, description = str, cost = float):
        self._id=id
        self._object=object
        self._weigth=weight
        self._description=description
        self._cost=cost
class OverweightPackage(Package):
    def __init__(self, id=int, objects=[Object], weight=0, description=str, cost=float):
        super().__init__(id, objects, weight, description, cost)
        self.overweigth_cost=cost
class StandardPackage(Package):
    def __init__(self, id=int, objects=[Object], weight=0, description=str, cost=float):
        super().__init__(id, objects, weight, description, cost)
class Adress:
    def __init__(self, st = str,city = str, hood = str, country = str, PC = int):
        self._st=st
        self._city=city
        self._hood=hood
        self._country=country
        self._PC=PC  
class Person:
    def __init__(self, name=str, id=int, adress = [Adress], phone = int):
        self._name=name
        self._id=id
        self._adress=adress
        self._phone=phone
class Deliver:
    def __init__(self,id=int,date=int,time=int,sender=Person,reciver=Person,sender_add=Adress,reciver_add=Adress,contact=Person,items=[Package]):
        self._id=id
        self._date=date
        self._time=time
        self._sender=sender
        self._reciver=reciver
        self._sender_add=sender_add
        self._reciver_add=reciver_add
        self._contact=contact
        self._items=items