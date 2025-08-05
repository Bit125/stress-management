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

    def get_reports_of_user(self, user, reports):
        reports_found = []

        #finding reports with a matching user ID
        for i in reports:
            if i.user_id == user.user_id:
                reports_found += i

        return reports_found

    def get_reports_on_date(self, date, reports):
        reports_found = []

        #finding reports with a matching date
        for i in reports:
            if i.date_and_time.date() == date:
                reports_found += i

        return reports_found
