# Jorge Andres Gandara Oliveros T00065470
class Package:
    def __init__(self, id = int, weight = 0, cost_per_gram = float, description = str, delivery_fee = float):
        self._id=id
        self._weigth=weight
        self._description=description
        self._cost_per_gram=cost_per_gram
    def calculate(self):
        return self._weigth * self._cost_per_gram
class StandardPackage(Package):
    def __init__(self, id=int, weight=0, cost_per_gram=float, description=str, delivery_fee=float):
        super().__init__(id, weight, cost_per_gram, description)
        self.delivery_fee = max(delivery_fee,0)
    def calculate(self):
        return super().calculate() + self.delivery_fee 
class OverweightPackage(Package):
    def __init__(self, id=int, weight=0, cost_per_gram=float, description=str, overweight_cost_per_gram=float):
        super().__init__(id, weight, cost_per_gram, description)
        self.overweight_cost_per_gram = max(overweight_cost_per_gram, 0)
    def calculate(self):
        if self.weight <= 1000:
            return super().calculate()
        else:
            overweight = self.weight - 1000
            overweight_cost = overweight * self.overweight_cost_per_gram
            return super().calculate() + overweight_cost
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
