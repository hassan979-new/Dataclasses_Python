from dataclasses import dataclass, asdict
import json
@dataclass(frozen=True,slots=True, order=True)
class Livre:
    titre:str
    auteur:str
    annee:int
    prix:float

    def promo(self, prix_reduit):
        return Livre(self.titre, self.auteur, self.annee,prix=prix_reduit)

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)
    
def charger_json(livre_json):
    return Livre(**json.loads(livre_json))