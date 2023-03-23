# Jorge Andres Gandara Oliveros T00065470
class Package:
    id = int
    weight = 0
    description = str
    cost = float
    W_GR_100 = 1
class Adress:
    st = str
    city = str
    hood = str
    country = str
    PC = int
class Person:
    name=str
    id=int
    adress = [Adress]
    phone = int
class Deliver:
    id=int
    date=int
    time=int
    sender=Person
    reciver=Person
    sender_add=Adress
    reciver_add=Adress
    contact=Person
    items=[Package]