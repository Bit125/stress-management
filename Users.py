class Users:
    def __init__(self, username, password, user_id, age, sex):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.age = age
        self.sex = sex

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

