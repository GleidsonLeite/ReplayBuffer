from dataclasses import asdict, dataclass
from typing import Dict, List
from bson import ObjectId


@dataclass
class Transition:
    execution_id: str
    episode: int
    step: int
    state: List[float]
    action: List[float]
    reward: float
    next_state: List[float]
    done: bool
    _id: ObjectId = None

    @property
    def as_dict(self) -> Dict:
        transition_dict = asdict(self)
        del transition_dict["_id"]
        transition_dict["_id"] = str(self._id)
        return transition_dict
