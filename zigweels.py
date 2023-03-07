from pprint import pprint

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


class ChromeBrowserAutomation:

    def __init__(self):
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        self.options = Options()
        self.options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options,
                                       desired_capabilities=desired_capabilities)

    def main(self):
        self.driver.get("https://www.zigwheels.com/")
        self.driver.maximize_window()

        search_input = self.driver.find_element(By.NAME, 'bysearch')
        search_input.send_keys("Creta")
        search_btn = self.driver.find_element(By.CSS_SELECTOR,
                                              'span[onclick="getByHeaderSearch($(\'#headerSearch\').val());"]')
        search_btn.click()

        sleep(30)
        entries = self.driver.execute_script('return performance.getEntries();')

        for entry in entries:
            if entry['name'] == 'https://adservice.google.co.in/adsid/integrator.js?domain=www.zigwheels.com':
                print(entry['duration'])

        # log_entries = self.driver.get_log("performance")
        # for log_data in log_entries:
        #     temp_str = str(log_data["message"])
        #     if temp_str.__contains__('https://adservice.google.co.in/adsid/integrator.js?domain=www.zigwheels.com'):
        #         pprint(type(log_data['message']))


if __name__ == '__main__':
    obj = ChromeBrowserAutomation()
    obj.main()

"""
execute_script

return performance.getentries


{'connectEnd': 1805, 'connectStart': 1689.5999999940395, 'decodedBodySize': 107,
        'domainLookupEnd': 1689.5999999940395, 'domainLookupStart': 1684.0999999940395, 'duration': 194.29999999701977,
        'encodedBodySize': 100, 'entryType': 'resource', 'fetchStart': 1683.2999999970198, 'initiatorType': 'link',
        'name': 'https://adservice.google.co.in/adsid/integrator.js?domain=www.zigwheels.com', 'nextHopProtocol': 'h2',
        'redirectEnd': 0, 'redirectStart': 0, 'renderBlockingStatus': 'non-blocking',
        'requestStart': 1806.0999999940395, 'responseEnd': 1877.5999999940395, 'responseStart': 1875.5999999940395,
        'responseStatus': 0, 'secureConnectionStart': 1708.5, 'serverTiming': [], 'startTime': 1683.2999999970198,
        'transferSize': 400, 'workerStart': 0}
"""
