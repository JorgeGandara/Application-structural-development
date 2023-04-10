from package import Package

#we define the OverweightPackage class that will inherit the attributes and functions of the Package class
class OverweightPackage(Package):
    #the constructor of each of the package attributes is created
    def __init__(self, id: int = 0, weight: float = 0.0, description: str = "description", cost_per_gram: float = 0.0, overweight_cost_per_gram: float = 0.0):
        #with the super() function we can inherit the attributes of the package class
        super().__init__(id, weight, description, cost_per_gram)
        self.overweight_cost_per_gram = overweight_cost_per_gram
      
    #This function is created to be able to modify the cost attribute of the weight per gram
    @property
    def overweight_cost_per_gram(self) -> float:
        return self._overweight_cost_per_gram

    @overweight_cost_per_gram.setter
    def overweight_cost_per_gram(self, overweight_cost_per_gram) -> float:
        self._overweight_cost_per_gram = overweight_cost_per_gram

    #the calculate function is defined to calculate the shipping cost of the product taking into account an extra cost if the product exceeds the weight
    def calculate(self):
        if self.weight > 50:
            overweight_cost = (self.weight - 50) * self.overweight_cost_per_gram
            return super().calculate() + overweight_cost
        else:
            return super().calculate()
          
    #We define the function that will allow us to print each of the attributes
    def __str__(self):
        return f"OverweightPackage: {self.id} - {self.weight}g - {self.description} - ${self.cost_per_gram}/g + ${self.overweight_cost_per_gram} overweight_cost" 

    #We define the equal function that will compare two objects
    def equals(self, other):
        if isinstance(other, OverweightPackage):
            return super().equals(other) and self.overweight_cost_per_gram == other.overweight_cost_per_gram
        return False