import pandas as pd 

# Prosty DataFrame 
drink = pd.DataFrame({
    'Napoje': ['Kawa', 'Herbata', 'Kakao'],
    'Cena': [10, 8, 9]
})

print(drink)


print("------")


# Walidacja 
class Drink ():
    def __init__(self, name_drink, price):
        if not isinstance(price, int):
            raise ValueError('Cena musi być w formacie int')
        self.name_drink = name_drink
        self.price = price

    def __str__(self):
        return f'Napój {self.name_drink} kosztuje {self.price} zł'
    
coffee = Drink("Kawa", 10)
tea = Drink("Herbata", 8)
cacao = Drink("Kakao", 9)

drink_walidation = pd.DataFrame({
    'Napoje': [coffee.name_drink, tea.name_drink, cacao.name_drink],
    "Cena": [coffee.price, tea.price, cacao.price]
})

print(drink_walidation)


print("------")

# Domyślny parametr
class EnergyDrink ():

    def __init__(self, buy='Brak produktu'):
        self.buy = buy


drinkOne = EnergyDrink('Tiger')
drinkTwo = EnergyDrink()

print(drinkOne.buy)
print(drinkTwo.buy)

print("------")

# Prywatny
class Smoothie ():

    def __init__(self, name_smoothie, __price_smoothie):
        self.name_smoothie = name_smoothie
        self.__price_smoothie = __price_smoothie


smoothieOne = Smoothie('Mango', 5)

print(smoothieOne.name_smoothie)