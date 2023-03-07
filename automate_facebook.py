
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep



class AutomateFacebook:

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def main(self, website):
        self.driver.get(website)
        # self.driver.maximize_window()

        self.driver.find_element(By.LINK_TEXT, "Create new account").click()
        sleep(2)


        first_name = self.driver.find_element(By.NAME, "firstname")
        first_name.send_keys("Ajay")
        self.driver.find_element(By.NAME, "lastname").send_keys("Bhandwalkar")
        self.driver.find_element(By.NAME, "reg_email__").send_keys("admin@admin.com")
        self.driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("admin@admin.com")
        self.driver.find_element(By.NAME, "reg_passwd__").send_keys("12@klSojkei8564.45")
        sleep(1)
        self.driver.find_element(By.NAME, "birthday_day").send_keys("12")
        self.driver.find_element(By.NAME, "birthday_month").send_keys("Sep")
        self.driver.find_element(By.NAME, "birthday_year").send_keys("1997")
        self.driver.find_element(By.XPATH, "//input[@value = '2']").click()
        self.driver.find_element(By.NAME, "websubmit")
        # self.driver.find_element(By.LINK_TEXT, "Sign Up").click()

        # self.driver.find_element(By.ID, "u_2_b_vy")
        # self.driver.find_element(By.CLASS_NAME, "inputtext _58mg _5dba _2ph-")


if __name__ == '__main__':
    af = AutomateFacebook()
    website = "https://www.facebook.com"
    af.main(website)
