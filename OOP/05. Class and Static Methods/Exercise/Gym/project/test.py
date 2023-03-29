from ss.customer import Customer
from ss.equipment import Equipment
from ss.exercise_plan import ExercisePlan
from ss.gym import Gym
from ss.subscription import Subscription
from ss.trainer import Trainer

ExercisePlan.id = 1
p = ExercisePlan.from_hours(1, 1, 16)
print(p.id)  # 1
print(p.trainer_id)  # 1
print(p.equipment_id)  # 1
print(p.duration)  # 960
