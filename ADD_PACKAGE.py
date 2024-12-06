from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Credentials and URL
url = "https://ecspro-qa.kloudship.com"
username = "kloudship.qa.automation@mailinator.com"
password = "Password1"

# Setup ChromeDriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 50)

try:
    print("Starting the browser and navigating to the URL...")
    driver.get(url)

    # Step 1: Login
    print("Logging in...")
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    # Verify login success
    try:
        print("Verifying login...")
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Package Types")))
        print("Login successful!")
    except Exception as e:
        print("Login failed. Exiting...")
        raise e

    # Step 2: Navigate to Package Types
    print("Navigating to Package Types...")
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Package Types"))).click()

    # Step 3: Click on Add Manually button
    print("Clicking Add Manually...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Add Manually']"))).click()

    # Step 4: Fill in the package details
    print("Filling in the package details...")
    random_dimension = random.randint(1, 20)
    wait.until(EC.presence_of_element_located((By.ID, "package-name"))).send_keys("FirstName_LastName")
    wait.until(EC.presence_of_element_located((By.ID, "package-dimensions"))).send_keys(random_dimension)

    # Save the package
    print("Saving the package...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()

    # Confirm success
    print("Confirming package creation...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Package added successfully')]")))

    # Step 5: Logout
    print("Logging out...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Logout']"))).click()

    print("Test case executed successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Closing the browser...")
    driver.quit()

