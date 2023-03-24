#from dearpygui.dearpygui import *
from model.user import User

class User_Ctrl:
    def __init__(self) -> None:
        self.users = []
    
    def create_user(self, user_id, user_name, user_email):
        self.user = User(user_id, user_name, user_email)
        self.users.append(self.user)

    def update_user(self, index, datatype, data):
        if datatype == "Name":
            self.users[index].set_name(data)
        elif datatype == "Email":
            self.users[index].set_email(data)
        else:
            print("Error")
        return self.users

    def delete_user(self, id):
        del self.users[id]
        return self.users