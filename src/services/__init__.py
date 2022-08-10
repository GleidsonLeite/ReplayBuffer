from typing import List
from src.repositories import TransitionsRepository
from bson import ObjectId


class CreateTransitionService:
    def __init__(self, transitions_repository: TransitionsRepository) -> None:
        self.__transitions_repository = transitions_repository

    def execute(
        self,
        execution_id: str,
        episode: int,
        step: int,
        state: List[float],
        action: List[float],
        reward: float,
        next_state: List[float],
        done: bool,
    ) -> str:
        return self.__transitions_repository.create(
            action=action,
            done=done,
            episode=episode,
            execution_id=execution_id,
            next_state=next_state,
            reward=reward,
            state=state,
            step=step,
        )
