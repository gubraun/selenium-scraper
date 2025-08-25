from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  

print("Start display...")
display.start()

print("Install Chromedriver...")
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

print("Set driver options...")
chrome_options = webdriver.ChromeOptions()
# Add your options as needed
options = [
   # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
    #"--headless",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    # These flags BELOW are recommended for stability when running Chrome in headless or containerized environments (such as GitHub Actions).
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    '--remote-debugging-port=9222'
]
for option in options:
    chrome_options.add_argument(option)

print("Start driver...")    
driver = webdriver.Chrome(options = chrome_options)

#driver.get("https://www.github.com")
driver.get("https://www.autosecurite.com")
print(driver.title)
