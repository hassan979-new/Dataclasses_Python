from film import Film

film1 = Film("Inception", "Nolan", 2010, 8.8)
film2 = Film("Matrix", "Wachowski", 1999, 9.0)

print(film1.to_json())
print(film2.est_classique())
print(film1 < film2)

json_str = film1.to_json()
film3 = Film.from_json(json_str)
print(film3)