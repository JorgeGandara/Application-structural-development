from package import Package
#Define the delivery class, this one will be in charge of delivering action, this class will also call the person class and the address class
class Delivery:
    #Constructor
    def __init__(self, item: str = "item", sender: str = "sender", receiver: str = "receiver", sender_address: str = "sender_address", receiver_address: str = "receiver_address", contact: str = "contact", date: str = "date", time: float = 0.0):
        self.items = []
        for package in item:
            if isinstance(package, Package):
                self.items.append(package)
        self.sender = sender
        self.receive = receiver
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.contact = contact
        self.date = date
        self.time = time
      
    #Here we create get and set for each attribute, for this we have to include sender and recivere attributes.
    @property
    def items(self) -> str:
        return self._items

    @items.setter
    def items(self, items) -> str:
        self._items = []
        for package in items:
            if isinstance(package, Package):
                self._items.append(package)

    @property
    def sender(self) -> str:
        return self._sender

    @sender.setter
    def sender(self, sender) -> str:
        self._sender = sender

    @property
    def receive(self) -> str:
        return self._receive

    @receive.setter
    def receive(self, receive) -> str:
        self._receive = receive

    @property
    def sender_address(self) -> str:
        return self._sender_address

    @sender_address.setter
    def sender_address(self, sender_address) -> str:
        self._sender_address = sender_address

    @property
    def receiver_address(self) -> str:
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address) -> str:
        self._receiver_address = receiver_address
      
    #We define these set and get functions in order to be able to change the time, date and contact attributes.
    @property
    def contact(self) -> str:
        return self._contact

    @contact.setter
    def contact(self, contact) -> str:
        self._contact = contact

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, date) -> str:
        self._date = date

    @property
    def time(self) -> float:
        return self._time

    @time.setter
    def time(self, time) -> float:
        self._time = time