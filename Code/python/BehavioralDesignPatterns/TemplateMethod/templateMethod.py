from abc import ABC, abstractmethod


# *********************************************************************
# Abstract Class
class BeverageMarker(ABC):
    def makeBeverage(self) -> None:
        self.boilWater()
        self.brew()
        self.pourCup()
        self.addCondiments()

    @abstractmethod
    def brew(self) -> None:
        pass

    @abstractmethod
    def addCondiments(self) -> None:
        pass

    def pourCup(self) -> None:
        print("Pouring into cup")

    def boilWater(self) -> None:
        print("Boiling water")


# *********************************************************************
# Concrete Class
class TeaMaker(BeverageMarker):
    def brew(self):
        print("Steeping the tea")

    def addCondiments(self):
        print("Adding lemon")


class CoffeeMaker(BeverageMarker):
    def brew(self):
        print("Dripping coffee through filter")

    def addCondiments(self):
        print("Adding sugar and milk")


# *********************************************************************
# Use
print("---- Making tea")
teaMaker: BeverageMarker = TeaMaker()
teaMaker.makeBeverage()

print("---- Making coffee")
coffeeMaker: BeverageMarker = CoffeeMaker()
coffeeMaker.makeBeverage()
