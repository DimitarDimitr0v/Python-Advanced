from calendar import month_name
class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_number: int, name: str, date: str, age_restriction: int):  # date format => dd.mm.yyyy
        day, month, year = [int(x) for x in date.split(".")]

        return cls(name, id_number, year, month_name[month], age_restriction)


    def __repr__(self):
        if self.is_rented:
            return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: rented"
        else:
            return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: not rented"
