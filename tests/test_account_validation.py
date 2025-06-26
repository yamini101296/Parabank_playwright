from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger()

def test_account_summary_check(page):
    login = LoginPage(page)
    login.load()
    login.login("john", "demo")  # Replace with valid credentials
    page.click("text=Accounts Overview")
    assert "Account Number" in page.content()
    logger.info("Account summary validation passed.")
