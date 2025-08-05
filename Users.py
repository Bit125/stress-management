class Users:
    def __init__(self, username, password, user_id, age, sex):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.age = age
        self.sex = sex
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