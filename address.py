#This class's purpose is to request the adress of both the sender and the reciever
class Address():
    #Here we create the constructor of each of the atributes 
    def __init__(self, address: str = "address"):
        self.address = address 
      
    #we create the get and set to obtain the sender's address
    @property
    def sender_add(self) -> str:
        return self.address
    
    @sender_add.setter
    def sender_add(self, address) -> str:
        self.address = address
      
    #we create the get and set to obtain the reciever's address       
    @property
    def receive_add(self) -> str:
        return self.address
    
    @receive_add.setter
    def receive_add(self, address) -> str:
        self.address = address