from package import Package
from standardPackage import StandardPackage
from address import Address
from person import Person
from delivery import Delivery
from overWeightPackage import OverweightPackage


# Define 5 packages with their information
package1 = StandardPackage(2534, 200, "Iphone", 5)
package2 = OverweightPackage(1547, 50000, "Sofa", 5, 10)
package3 = OverweightPackage(7894, 77000, "Nevera", 5, 15)
package4 = StandardPackage(5789, 2000, "Laptop", 5)
package5 = Package(7948, 1000, "Cafetera", 5)

# Define source and destination address
sender_address = Address("Av. Boyacá #80-94, Bogotá")
receiver_address = Address("Cra 93 #77 Cartagena")

# Define a person who receives and a person that sends
sender = Person("Robert", "Pantoja", "+57 3103723842")
receiver = Person("Jorge", "Gandara", "+57 3103452341")

# Define a shipment using the packages, addresses and the people we defined before
shipment = Delivery([package1, package2, package3], sender, receiver, sender_address, receiver_address, "+57 3103452341", "2023-03-25", "10:00")

print("\nInvolucrados:\n")
print(f"Remitente: {shipment.sender.sender} - Contacto: {shipment.sender.contact} - Dirección: {shipment.sender_address.sender_add}")
print(f"Receptor: {shipment.receive.receiver} - Contacto: {shipment.receive.contact} - Dirección: {shipment.receiver_address.sender_add}")
print("\nProductos:\n")
for item in shipment.items:
    print(item)
print(f"\nFecha de entrega: {shipment.date} - Hora de entrega: {shipment.time} - Contacto: {shipment.contact}")