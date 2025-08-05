import matplotlib.pyplot as plt
import numpy as np

class Management:
    def __init__(self):
        self.users = []
        self.reports = []
        self.repots_number = 0
        self.users_number = 0

    def getUserRepot(self):
        return self.reports

    def addReport(self,report):
        self.reports.append(report)

    def viewAllUserReport(self, id):
        # for i in range(self.repots_number):
        #     if id == self.reports[i].user_id:

    #def getUser
