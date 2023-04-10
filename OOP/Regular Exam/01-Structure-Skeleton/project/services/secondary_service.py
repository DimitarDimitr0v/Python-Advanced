from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):

        static_capacity = 15
        super().__init__(name, static_capacity)
        self.capacity = static_capacity


    def details(self):
        result = f"{self.name} Secondary Service:\n"

        if self.robots:
            result += f"Robots: {', '.join([x.name for x in self.robots])}"
        else:
            result += "Robots: none"

        return result
