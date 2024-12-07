from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Constants
URL = "https://ecspro-qa.kloudship.com"
USERNAME = "kloudship.qa.automation@mailinator.com"
PASSWORD = "Password1"
def safe_find(driver, locator):
    """Safely find an element with a timeout."""
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
driver = webdriver.Chrome()  # Ensure correct WebDriver is used
driver.get(URL)
# Login
safe_find(driver, (By.ID, "login-email")).send_keys(USERNAME)
safe_find(driver, (By.ID, "login-password")).send_keys(PASSWORD)
safe_find(driver, (By.ID, "login-btn")).click()
wait = WebDriverWait(driver, 5)
# Delete Package
safe_find(driver, (By.CSS_SELECTOR, ".text-count-card.wordwrap-none")).click()
safe_find(driver, (By.CSS_SELECTOR, ".mat-focus-indicator.mat-menu-trigger.mat-tooltip-trigger.header-button.mat-icon-button.mat-button-base")).click()
safe_find(driver, (By.XPATH, "//button[contains(text(), ' Newest First ')]")).click()
print(f"Package deleted successfully!")
#loged out
safe_find(driver, (By.CSS_SELECTOR, ".mat-focus-indicator.mat-menu-trigger.mat-tooltip-trigger.mat-icon-button.mat-button-base")).click()
safe_find(driver, (By.CSS_SELECTOR, ".mat-focus-indicator.mat-menu-item.ng-tns-c99-1")).click()
print("Logged Out Succesfully")
