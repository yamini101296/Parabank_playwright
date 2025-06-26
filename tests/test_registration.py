from pages.registration_page import RegistrationPage
from utils.logger import setup_logger

logger = setup_logger()

def test_register_new_user(page):
    register = RegistrationPage(page)
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    register.register("Jane", "Doe", "janedoe123", "janepass123")
    assert "Your account was created successfully." in page.content()
    logger.info("Registration test passed.")
