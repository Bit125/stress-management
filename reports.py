import datetime
import time

class Report:
    def __init__(self, level, user):
        self.stress_level = level
        self.user_id = user
        #the date AND time of the report
        self.date_and_time = datetime.datetime.now()