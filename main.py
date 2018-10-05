from selenium import webdriver

# You must enable the 'Allow Remote Automation' option in Safari's Develop menu to control Safari via WebDriver.

# Major options are Firefox, Chrome, Safari
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Safari()
# Tell webdriver we'll wait for up to 5 seconds to wait for elements to appear
browser.implicitly_wait(1)

browser.get('https://www.hanzo.co')

assert browser.save_screenshot('./images/load.png')

try:
    browser.find_element_by_css_selector(".doesNotExistHere")
except NoSuchElementException:
    print("Element didn't exist!")

browser.find_element_by_css_selector("#hs-eu-confirmation-button").click()

assert browser.save_screenshot('./images/clicked_accept_cookies.png')

partial_link_text = "Technolo"
element = browser.find_element_by_partial_link_text(partial_link_text)
print("Found a link by partial link text '{}': {}".format(partial_link_text, element.text))

print("Number of a elements: {}".format(len(browser.find_elements_by_css_selector("a"))))

browser.close()
