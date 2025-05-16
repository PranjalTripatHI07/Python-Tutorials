class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def user_details(self):
        user_info = f"\n  Full Name= {self.first_name} {self.last_name}"
        return user_info.title()


class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("\n List of privileges")
        for privilege in self.privileges:
            print(f"-{privilege}")


class Admin(Users):
    def __init__(self, first_name, last_name, *privileges):
        super().__init__(first_name, last_name)
        self.privilege = Privileges(*privileges)

