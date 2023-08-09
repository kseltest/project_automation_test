
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from TestData import credentials

from TestLocators.add_employee import AddEmployeeLocators


class AddEmployeeActions:

    def __init__(self):
        self.addlocators = AddEmployeeLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def pim(self):
        pim_webelement = self.driver.find_element(By.XPATH, self.addlocators.pim_module)
        pim_webelement.click()

    def add_employee_information(self):
        """
        find the webelement for employee to add new employee
        :return:
        """

        add_employee_webelement = self.driver.find_element(By.XPATH, self.addlocators.add_employee_button)
        add_employee_webelement.click()
        sleep(3)

        first_name_webelement = self.driver.find_element(By.XPATH, self.addlocators.employee_first_name)
        first_name_webelement.clear()
        first_name_webelement.send_keys(credentials.employee_first_name)
        sleep(2)

        last_name_webelement = self.driver.find_element(By.XPATH, self.addlocators.employee_last_name)
        last_name_webelement.clear()
        last_name_webelement.send_keys(credentials.employee_last_name)
        sleep(2)


        save_button_webelement = self.driver.find_element(By.XPATH, self.addlocators.employee_save_button)
        save_button_webelement.click()

    def login_to_orangehrm(self):
        self.set_username()
        self.set_password()
        self.click_login()
        sleep(3)

    def add_success_message(self):
        success_message = "Successfully Saved "
        return success_message
    # return self.driver.edit_employee_success_message
    # return self.driver.dashboard
