import matplotlib.pyplot as plt
import numpy as np

class Users:
    def __init__(self, username, password, user_id, age, sex):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.age = age
        self.sex = sex
        self.reports = []
        self.logged_in = False

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_id(self):
        return self.user_id

    def get_age(self):
        return self.age

    def get_sed(self):
        return self.sex

    def set_username(self, new_username):
        self.username = new_username

    def set_password(self, new_password):
        self.password = new_password

    def set_user_id(self, new_user_id):
        self.user_id = new_user_id

    def set_age(self, new_age):
        self.age = new_age

    def set_sex(self, new_sex):
        self.sex = new_sex

    def log_in(self, password):
        if  password == self.password:
            self.logged_in = True
            print("Login successful.")
        else:
            self.logged_in = False
            print("Login failed. Incorrect username or password.")

        return self.logged_in

    def add_report(self,report):
        self.reports.append(report)


    def view_report(self, reports_inp):
        if len(reports_inp) == 0:
            return

        plt.style.use('_mpl-gallery')

        y = []
        x = []
        n = 0
        for i in range(len(reports_inp)):
            y.append(reports_inp[n].stress_level)
            x.append(n)

            n = n + 1

        # plot
        fig, ax = plt.subplots()

        ax.plot(x, y)

        ax.set(xlim=(0, n), xticks=np.arange(1, n),
               ylim=(0, 12), yticks=np.arange(1, 12))

        plt.show()

    def view_user_report(self, identifier):

        if len(self.reports) == 0:
            return

        plt.style.use('_mpl-gallery')

        y = []
        x = []
        n = 0
        for i in range(len(self.reports)):
            if identifier == self.reports[i].user_id:

                y.append(self.reports[n].stress_level)
                x.append(n)

                n = n + 1

        # plot
        fig, ax = plt.subplots()

        ax.plot(x, y)

        ax.set(xlim=(0, n), xticks=np.arange(1, n),
               ylim=(0, 12), yticks=np.arange(1, 12))

        plt.show()


