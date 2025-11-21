
# 🧮 Exceptions

## 📘 Description

Cette série de projets Python explore les dataclasses et leur utilisation avancée :

- Définition de classes immuables avec @dataclass(frozen=True, slots=True, order=True)

- Sérialisation et désérialisation en JSON (to_json, from_json)

- Comparaison d’objets grâce à l’option order=True

- Méthodes spécialisées pour enrichir les comportements métier (promo, est_classique)

- Encapsulation stricte et manipulation d’objets dans des contextes concrets (livres, films)

## 📂 Project Structure
````
projets/
├── Exercice1/
│   ├── livre.py
│   └── main.py
├── Exercice2/
│   ├── film.py
│   └── main.py
└── README.md
````


## ⚙️ Features

### **1.** Livre – Sérialisation et promotion
Classe Livre

- Attributs : titre, auteur, annee, prix

Méthodes :

- promo(prix_reduit) : retourne un nouvel objet Livre avec prix réduit

- to_json() : sérialise l’objet en JSON

- Comparaison : activée par order=True (permet <, > entre livres)

Fonction externe

- charger_json(livre_json) : désérialise une chaîne JSON en objet Livre

Programme principal

- Création d’un livre

- Sérialisation et désérialisation en JSON

- Application d’une promotion

- Comparaison entre livres

### **2.** Film – Sérialisation et classification
Classe Film

- Attributs : titre, realisateur, annee, note

- Particularité : titre, realisateur, annee exclus de la comparaison (compare=False)

Méthodes :

- to_json() : sérialise l’objet en JSON

- est_classique() : retourne True si année < 2000

- from_json(chain_json) : méthode de classe pour désérialiser un film

Programme principal

- Création de films

- Sérialisation en JSON

- Vérification si un film est classique

- Comparaison entre films (basée sur note)

- Désérialisation d’un film à partir de JSON
## 🖥️ Example Execution

### Exercice1 :
- <img width="480" height="504" alt="image" src="https://github.com/user-attachments/assets/cc0eb7d7-9c61-41c4-8f91-21774311b2d4" />
### Exercice2 : 
- <img width="480" height="504" alt="image" src="https://github.com/user-attachments/assets/0f27000b-1610-4b22-8b0a-2b79138bf5da" />
## 💡 Concepts Practiced

- Utiliser les dataclasses pour simplifier la définition des classes

- Exploiter les options avancées (frozen, slots, order) pour contrôler immuabilité, mémoire et comparaison

- Sérialiser et désérialiser des objets avec le module json

- Personnaliser la logique métier avec des méthodes spécialisées (promo, est_classique)

- Structurer le code en modules clairs et réutilisables

## 🧑‍💻 Author

- 👤 Agouram Hassan
- 🏫 Programmation orientée objet : python
- 🎓 Instructor	Mr.LACHGAR
- 📅 21	novembre 2025
