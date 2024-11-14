import os
from datetime import datetime
import pytest
from selenium import webdriver
from utils.config import BASE_URL

@pytest.fixture
def driver():
    #At the beginning of the test case
    driver_option = webdriver.ChromeOptions()
    driver_option.add_argument("--start-maximized")
    driver = webdriver.Chrome( options=driver_option)
    driver.get(BASE_URL)
    driver.set_page_load_timeout(30)  # Wait for 30 seconds for page load

    #This will be called when the test case is over
    yield driver
    driver.quit()

@pytest.fixture
def open_home_page(driver):
    driver.get(BASE_URL)
    return driver


def pytest_configure(config):
    # Create a reports directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Generate a timestamped filename
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    report_path = f"reports/report_{timestamp}.html"

    # Set the report file path in pytest config options
    config.option.htmlpath = report_path