from selenium.webdriver.common.by import By

from pages.Page_search import txt_search, btn_search


class stepSearch:
    def __init__(self, driver):
        self.driver = driver

    # ACTIONS
    def search(self, keyword):
        print("[Step] Search")
        self.inputKeyword(keyword)
        self.clickButtonSearch()

    def inputKeyword(self, keyword):
        print("[+] Input keyword")
        self.get_txtSearch().send_keys(keyword)

    def clickButtonSearch(self):
        print("[+] Click button search")
        self.get_btnSearch().click()

    # GET ELEMENT
    def get_txtSearch(self):
        return self.driver.find_element(By.XPATH, txt_search())

    def get_btnSearch(self):
        return self.driver.find_element(By.XPATH, btn_search())
