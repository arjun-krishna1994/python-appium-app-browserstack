from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",

    # Set URL of the application under test
    "app" : "bs://2c0b123313f86b2f94328490921736c14883f5cb",

    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "First Azurre Python project",
        "buildName" : "browserstack-build-azure-1",
        "sessionName" : "BStack azure_first_test",

        # Set your access credentials
        "userName" : os.getenv("BROWSERSTACK_USERNAME"),
        "accessKey" : os.getenv("BROWSERSTACK_ACCESS_KEY")
    }
})

# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

# Test case for the BrowserStack sample Android app.
# If you have uploaded your app, update the test case here.
search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()
search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(5)
search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
assert (len(search_results) > 0)

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
