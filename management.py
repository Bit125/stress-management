import matplotlib.pyplot as plt
import numpy as np

from reports import Report

class Management:
    def __init__(self):
        self.users = []
        self.reports = []
        self.repots_number = 0
        self.users_number = 0

    def get_user_reports(self):
        return self.reports

    def add_report(self,report):
        self.reports.append(report)

    def view_user_report(self, id):
        plt.style.use('_mpl-gallery')

        ay = []

        for i in range(self.repots_number):
            if id == self.reports[i].user_id:
                ay.append(self.reports[i].stress_level)

        # make data
        x = np.arange(0, 10, 2)
        y = ay

        # plot
        fig, ax = plt.subplots()

        ax.stackplot(x, y)

        ax.set(xlim=(0, 8), xticks=np.arange(1, 20),
               ylim=(0, 8), yticks=np.arange(1, 10))

        plt.show()



