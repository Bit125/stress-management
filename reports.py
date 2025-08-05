import datetime
import time

class Report:
    def __init__(self, level, user):
        self.stress_level = level
        self.user_id = user
        #the date AND time of the report
        self.date_and_time = datetime.datetime.now()

report1 = Report(8, 0)
print(report1.date_and_time)

time.sleep(5)
report2 = Report(2, 0)
print(report2.date_and_time)