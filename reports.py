import datetime
#import time

class Report:
    def __init__(self, level, user):
        self.stress_level = level
        self.user_id = user
        #the date AND time of the report
        self.date_and_time = datetime.datetime.now()

    #returns a string that tells you which report it is
    def __str__(self):
        return "User ID: " + str(self.user_id) + ", Time: " + str(self.date_and_time)

    def get_stress_level(self):
        return self.stress_level

    def get_user_id(self):
        return self.user_id

    def get_date_and_time(self):
        return self.date_and_time