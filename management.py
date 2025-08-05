import matplotlib.pyplot as plt
import numpy as np

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

    #def getUser

    def get_reports_of_user(self, user):
        reports_found = []
        for i in self.reports:
            if i.user_id == user.user_id:
                reports_found += i
