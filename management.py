import matplotlib.pyplot as plt
import numpy as np

class Management:
    def __init__(self):
        self.users = []
        self.reports = []
        self.repotsNumber = 0
        self.usersNumber = 0

    def getUserRepot(self):
        return self.reports

    def addReport(self,report):m
        self.reports.append(report)

    def viewAllUserReport(self, id):
        # for i in range(self.repotsNumber):
        #     if id == self.reports[i].a