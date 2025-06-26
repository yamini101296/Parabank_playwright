from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger()

def test_login_success(page):
    login = LoginPage(page)
    login.load()
    login.login("john", "demo")  # Replace with valid credentials
    assert "Accounts Overview" in page.content()
    logger.info("Login test passed.")
