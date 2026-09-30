
class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, userEmail, userPassword):
        self.page.locator("#userEmail").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name="login").click()
