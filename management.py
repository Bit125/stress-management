import matplotlib.pyplot as plt
import numpy as np

class Management:
    def __init__(self):
        users = []
        reports = []
        repotsNumber = 0
        usersNumber = 0

    def getUserRepot(self):
        return self.reports

    def addReport(self,report):
        self.reports.append(report)

