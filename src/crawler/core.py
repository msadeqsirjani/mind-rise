from src import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--user-data-dir=C:/Users/SQ-PC/AppData/Local/Google/Chrome/User Data")
options.add_argument("--profile-directory=Default")
options.add_argument("--disable-extensions")
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
