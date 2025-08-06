import matplotlib.pyplot as plt
import numpy as np
from Users import Users

class Management:
    def __init__(self):
        self.users = []
        #self.reports = []
        self.reports_number = 0
        self.users_number = 0

    def get_user_reports(self):
        return self.reports

    # def add_report(self,report):
    #     self.reports.append(report)
    #     self.reports_number += 1

    #
    # def view_report(self, reports_inp):
    #     if self.reports_number == 0:
    #         return
    #
    #     plt.style.use('_mpl-gallery')
    #
    #     y = []
    #     x = []
    #     n = 0
    #     for i in range(len(reports_inp)):
    #         y.append(reports_inp[n].stress_level)
    #         x.append(n)
    #
    #         n = n + 1
    #
    #     # make data
    #     # plot
    #     fig, ax = plt.subplots()
    #
    #     ax.plot(x, y)
    #
    #     ax.set(xlim=(0, n), xticks=np.arange(1, n),
    #            ylim=(0, 12), yticks=np.arange(1, 12))
    #
    #     plt.show()


    def add_user(self, username, password, age, sex):
        self.users_number += 1
        new_user = Users(username, password, self.users_number, age, sex)
        self.users.append(new_user)

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

