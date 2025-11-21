from dataclasses import dataclass, asdict, field
import json

@dataclass(frozen=True,slots=True, order=True)
class Film:
    titre:str = field(compare=False)
    realisateur:str = field(compare=False)
    annee:int = field(compare=False)
    note:float

    

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)
    
    def est_classique(self):
        # return True if self.annee<2000 else False
        return self.annee<2000
    
    @classmethod
    def from_json(cls,chain_json:str):
        return cls(**json.loads(chain_json))