class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.first_name = 'input[name="customer.firstName"]'
        self.last_name = 'input[name="customer.lastName"]'
        self.username = 'input[name="customer.username"]'
        self.password = 'input[name="customer.password"]'
        self.confirm = 'input[name="repeatedPassword"]'
        self.register_button = 'input[value="Register"]'

    def register(self, first, last, username, password):
        self.page.fill(self.first_name, first)
        self.page.fill(self.last_name, last)
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.fill(self.confirm, password)
        self.page.click(self.register_button)
