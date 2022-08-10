from typing import Any, Dict, List
from pymongo import MongoClient

from src.entities import Transition
from src.error import AppException


class TransitionsRepository:
    def __init__(self) -> None:
        self.__client = MongoClient(
            host="localhost", port=27017, username="root", password="example"
        )
        self.__database = self.__client.transition_database
        self.__collection = self.__database.transition_collection

    def create(
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
        transition_document = {
            "execution_id": execution_id,
            "episode": episode,
            "step": step,
            "state": state,
            "action": action,
            "reward": reward,
            "next_state": next_state,
            "done": done,
        }
        insert_one_response = self.__collection.insert_one(transition_document)
        return insert_one_response.inserted_id

    def list(self) -> List[Transition]:
        return self.find({})

    def drop(self) -> None:
        self.__collection.drop()

    def find_by_execution_id(self, execution_id: str) -> List[Transition]:
        return self.find({"execution_id": execution_id})

    def find(self, *args: Any, **kwargs: Any) -> List[Transition]:
        found_transitions = self.__collection.find(*args, **kwargs)
        return [
            Transition(**found_transition) for found_transition in found_transitions
        ]

    def count(self, filter: Dict = {}) -> int:
        return self.__collection.count_documents(filter)

    def count_by_execution_id(self, execution_id: str) -> int:
        return self.__collection.count_documents(
            {
                "execution_id": execution_id,
            }
        )

    def find_samples_from_execution_id(
        self, execution_id: str, number_of_samples: int
    ) -> List[Transition]:

        found_transitions = self.__collection.aggregate(
            [
                {"$match": {"execution_id": execution_id}},
                {"$sample": {"size": number_of_samples}},
            ]
        )

        return [
            Transition(**found_transition) for found_transition in found_transitions
        ]
