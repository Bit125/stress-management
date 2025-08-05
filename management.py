import matplotlib.pyplot as plt
import numpy as np
from Users import Users

class Management:
    def __init__(self):
        self.users = []
        self.reports = []
        self.repots_number = 0
        self.users_number = 0

    def get_user_report(self):
        return self.reports

    def add_report(self,report):
        self.reports.append(report)

    def view_user_report(self, id):
        # for i in range(self.repots_number):
        #     if id == self.reports[i].user_id:
        pass

    def add_user(self, username, password, age, sex):
        self.users_number += 1
        new_user = Users(username, password, self.users_number, age, sex)
        self.users.append(new_user)

    #def getUser
