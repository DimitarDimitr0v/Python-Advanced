from ss.caretaker import Caretaker
from ss.cheetah import Cheetah
from ss.keeper import Keeper
from ss.lion import Lion
from ss.tiger import Tiger
from ss.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if self.__budget - price >= 0 and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        elif self.__budget - price < 0:
            return "Not enough budget"

        return "Not enough space for animal"


    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return "Not enough space for worker"


    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]

        if worker:
            self.workers.pop()
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([x.salary for x in self.workers])

        if total_salaries <= self.__budget:
            left_budget = self.__budget - total_salaries
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {left_budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_take_care = sum(x.money_for_care for x in self.animals)

        if animal_take_care <= self.__budget:
            left_budget = self.__budget - animal_take_care
            self.__budget -= animal_take_care
            return f"You tended all the animals. They are happy. Budget left: {left_budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lion_objects = [l for l in self.animals if isinstance(l, Lion)]  # all lions in the zoo
        lion_info = '\n'.join([x.__repr__() for x in lion_objects])

        tiger_objects = [t for t in self.animals if isinstance(t, Tiger)]
        tiger_info = '\n'.join([x.__repr__() for x in tiger_objects])

        cheetah_objects = [c for c in self.animals if isinstance(c, Cheetah)]
        cheetah_info = '\n'.join([x.__repr__() for x in cheetah_objects])

        animal_status = f"You have {len(self.animals)} animals\n" \
                        f"----- {len(lion_objects)} Lions:\n" \
                        f"{lion_info}\n" \
                        f"----- {len(tiger_objects)} Tigers:\n" \
                        f"{tiger_info}\n" \
                        f"----- {len(cheetah_objects)} Cheetahs:\n" \
                        f"{cheetah_info}"

        return animal_status



    def workers_status(self):
        keeper_objects = [k for k in self.workers if isinstance(k, Keeper)]
        keeper_info = '\n'.join([x.__repr__() for x in keeper_objects])

        caretaker_objects = [c for c in self.workers if isinstance(c, Caretaker)]
        caretaker_info = '\n'.join([x.__repr__() for x in caretaker_objects])

        vet_objects = [v for v in self.workers if isinstance(v, Vet)]
        vet_info = '\n'.join([x.__repr__() for x in vet_objects])

        worker_status = f"You have {len(self.workers)} workers\n" \
                        f"----- {len(keeper_objects)} Keepers:\n" \
                        f"{keeper_info}\n" \
                        f"----- {len(caretaker_objects)} Caretakers:\n" \
                        f"{caretaker_info}\n" \
                        f"----- {len(vet_objects)} Vets:\n" \
                        f"{vet_info}"

        return worker_status
