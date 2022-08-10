from src.repositories import TransitionsRepository
from json import dumps

repository = TransitionsRepository()

created_transition_id = repository.create(
    action=[1, 2, 3, 4],
    done=True,
    episode=0,
    execution_id="12345",
    next_state=[1, 2, 3, 4],
    reward=0,
    state=[1, 2, 3, 4],
    step=0,
)

print(created_transition_id)

transitions = repository.find_samples_from_execution_id("12345", 2)

for transition in transitions:
    print(dumps(transition.as_dict))
