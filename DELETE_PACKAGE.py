from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException

# Setup ChromeDriver
options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
# Uncomment the following line to run in headless mode
# options.add_argument("--headless")

service = Service('chromedriver-win64\chromedriver.exe')  # Replace with your chromedriver path
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 35)

# Credentials
url = "https://ecspro-qa.kloudship.com"
username = "kloudship.qa.automation@mailinator.com"
password = "Password1"

try:
    print("Launching browser and navigating to URL...")
    driver.get(url)

    # Step 1: Login
    print("Logging in...")
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

    # Verify login success
    print("Verifying login success...")
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Package Types")))
    print("Login successful!")

    # Step 2: Navigate to Package Types
    print("Navigating to Package Types...")
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Package Types"))).click()

    # Step 3: Locate and Delete the Package
    print("Locating the package to delete...")
    package_name = "FirstName_LastName"  # Replace with the package name created in the first test
    package_row_xpath = f"//tr[td[contains(text(), '{package_name}')]]"

    try:
        # Locate the package row
        package_row = wait.until(EC.presence_of_element_located((By.XPATH, package_row_xpath)))
        print(f"Package '{package_name}' found. Deleting...")
        
        # Locate and click the delete button within the package row
        delete_button = package_row.find_element(By.XPATH, ".//button[contains(text(), 'Delete')]")
        delete_button.click()

        # Confirm deletion if a confirmation dialog appears
        confirm_button_xpath = "//button[contains(text(), 'Confirm')]"
        wait.until(EC.element_to_be_clickable((By.XPATH, confirm_button_xpath))).click()
        print(f"Package '{package_name}' deleted successfully!")
    except TimeoutException:
        print(f"Package '{package_name}' not found. Nothing to delete.")

    # Step 4: Logout
    print("Logging out...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Logout')]"))).click()
    print("Logged out successfully!")

except TimeoutException as te:
    print(f"TimeoutException: {te}")
except WebDriverException as we:
    print(f"WebDriverException: {we}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Closing the browser...")
    driver.quit()

