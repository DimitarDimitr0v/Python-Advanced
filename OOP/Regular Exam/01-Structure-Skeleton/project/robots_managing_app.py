from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []


    def add_service(self, service_type: str, name: str):

        if service_type == "MainService":
            service = MainService(name)
        elif service_type == "SecondaryService":
            service = SecondaryService(name)
        else:
            raise Exception("Invalid service type!")

        self.services.append(service)
        return f"{service_type} is successfully added."


    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
        elif robot_type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)
        else:
            raise Exception("Invalid robot type!")

        self.robots.append(robot)
        return f"{robot_type} is successfully added."


    def add_robot_to_service(self, robot_name: str, service_name: str):

        robot = [x for x in self.robots if x.name == robot_name][0]
        service = [x for x in self.services if x.name == service_name][0]

        if service.__class__.__name__ == "SecondaryService" and robot.__class__.__name__ == "MaleRobot":
            return "Unsuitable service."
        if service.__class__.__name__ == "MainService" and robot.__class__.__name__ == "FemaleRobot":
            return "Unsuitable service."

        if len(service.robots) + 1 > service.capacity:
            raise Exception("Not enough capacity for this robot!")


        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."


    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = [x for x in self.services if x.name == service_name][0]
        try:
            robot = [x for x in service.robots if x.name == robot_name][0]
        except IndexError:
            raise Exception("No such robot in this service!")


        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."


    def feed_all_robots_from_service(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]
        fed_robots_count = 0

        for robot in service.robots:
            robot.eating()
            fed_robots_count += 1

        return f"Robots fed: {fed_robots_count}."


    def service_price(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]
        total_price = 0

        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."


    def __str__(self):
        result = ""

        for i in range(len(self.services)):
            service = self.services[i]

            if i + 1 < len(self.services):
                result += f"{service.details()}\n"
            else:
                result += f"{service.details()}"

        return result

