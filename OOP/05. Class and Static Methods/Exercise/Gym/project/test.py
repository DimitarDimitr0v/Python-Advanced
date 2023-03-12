from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

ExercisePlan.id = 1
p = ExercisePlan.from_hours(1, 1, 16)
print(p.id)  # 1
print(p.trainer_id)  # 1
print(p.equipment_id)  # 1
print(p.duration)  # 960
