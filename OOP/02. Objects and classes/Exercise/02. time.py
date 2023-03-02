class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, upd_hrs, upd_mins, upd_secs):
        self.hours = upd_hrs
        self.minutes = upd_mins
        self.seconds = upd_secs

    def get_time(self) -> str:
        return f"{int(self.hours):02d}:{int(self.minutes):02d}:{int(self.seconds):02d}"

    def next_second(self) -> str:

        if self.seconds == Time.max_seconds:
            if self.minutes == Time.max_minutes:
                if self.hours == Time.max_hours:
                    self.seconds, self.minutes, self.hours = 0, 0, 0

                else:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours += 1
            else:
                self.seconds = 0
                self.minutes += 1
        else:
            self.seconds += 1

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(1, 20, 31)
print(time.next_second())
