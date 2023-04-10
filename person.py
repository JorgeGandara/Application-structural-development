#definition of the person class that will help us to determine the information of the sender and the sender
class Person():
    def __init__(self, name: str = "name", surname: str = "surname", contact: str = "contact"):
        self.name = name 
        self.contact = contact
        self.surname = surname

    #get and the set are done to get the name and surname of the sender
    @property
    def sender(self) -> str:
        return self.name
        return self.surname
    
    @sender.setter
    def sender(self, name, surname) -> str:
        self.name = name
        self.surname = surname 

    #get and the set are done to get the name and surname of the receiver  
    @property
    def receiver(self) -> str:
        return self.name
        return self.surname
    
    @receiver.setter
    def receiver(self, name, surname) -> str:
        self.name = name
        self.surname = surname

    #get and set are done for contact attribute  
    @property
    def contact(self) -> str:
        return self._contact
    
    @contact.setter
    def contact(self, contact) -> str:
        self._contact = contact