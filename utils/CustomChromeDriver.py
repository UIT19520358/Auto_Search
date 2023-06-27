from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def customChrome():
    ser = Service(r"../drivers/chromedriver.exe")

    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ser, options=options)

    print("[Open browser] Open google chrome browser")
    return driver
