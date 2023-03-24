class User:
    def __init__(
            self,
            id,
            name,
            email
            ):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"ID: {self.id},\nNome: {self.name},\nEmail: {self.email}"

    def set_id(self, int: id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email