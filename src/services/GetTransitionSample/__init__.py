from typing import List
from src.entities import Transition
from src.error import AppException
from src.repositories import TransitionsRepository


class GetTransitionSampleService:
    def __init__(self, transitions_repository: TransitionsRepository) -> None:
        self.__transitions_repository = transitions_repository

    def execute(
        self,
        execution_id: str,
        number_of_samples: int,
    ) -> List[Transition]:
        number_of_documents = self.__transitions_repository.count_by_execution_id(
            execution_id=execution_id
        )
        if number_of_documents == 0:
            raise AppException(
                "There are not transitions with the given execution_id",
                404,
            )
        are_there_enough_samples = number_of_documents >= number_of_samples

        if not are_there_enough_samples:
            raise AppException("The execution does not have enough samples")
        return self.__transitions_repository.find_samples_from_execution_id(
            execution_id=execution_id,
            number_of_samples=number_of_samples,
        )
