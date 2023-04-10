from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):

        static_capacity = 30
        super().__init__(name, static_capacity)
        self.capacity = static_capacity


    def details(self):
        result = f"{self.name} Main Service:\n"

        if self.robots:
            result += f"Robots: {', '.join([x.name for x in self.robots])}"
        else:
            result += "Robots: none"

        return result

