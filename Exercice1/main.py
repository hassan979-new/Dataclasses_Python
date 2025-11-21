from livre import Livre,charger_json

livre1 = Livre("1984", "George Orwell", 1949, 9.90)
livre_json = livre1.to_json()
livre2 = charger_json(livre_json)
livre3 = livre1.promo(7.50)

print(livre3<livre2)

print(livre1.to_json())
print(livre2.to_json())
print(livre3.to_json())