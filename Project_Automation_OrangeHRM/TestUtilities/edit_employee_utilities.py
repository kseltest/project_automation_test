
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from TestData import credentials

from TestLocators.edit_employee import EditEmployeeLocators


class EditEmployeeActions:

    def __init__(self):
        self.editlocators = EditEmployeeLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def pim(self):
        pim_webelement = self.driver.find_element(By.XPATH, self.editlocators.pim_module)
        pim_webelement.click()

    def employee_information(self):
        """
        find the webelement for employee to select and edit the information and then safe the details
        :return:
        """

        employee_name_webelement = self.driver.find_element(By.XPATH, self.editlocators.employee_name)
        employee_name_webelement.clear()
        employee_name_webelement.send_keys(credentials.employee_name)

        search_button_webelement = self.driver.find_element(By.XPATH, self.editlocators.search_button)
        search_button_webelement.click()
        sleep(3)

        # employee_list_webelement = self.driver.find_element(By.XPATH, self.editlocators.employee_list_button)
        # employee_list_webelement.click()

        select_employee_webelement = self.driver.find_element(By.XPATH, self.editlocators.select_employee_checkbox)
        select_employee_webelement.click()

        edit_employee_webelement = self.driver.find_element(By.XPATH, self.editlocators.employee_edit_icon)
        edit_employee_webelement.click()
        sleep(3)

        employee_name1_webelement = self.driver.find_element(By.XPATH, self.editlocators.employee_name1)
        employee_name1_webelement.clear()
        employee_name1_webelement.send_keys(credentials.employee_name1)

        save_button_webelement = self.driver.find_element(By.XPATH, self.editlocators.employee_edit_icon)
        save_button_webelement.click()

    # def login_to_orangehrm(self):
    #     self.set_username()
    #     self.set_password()
    #     self.click_login()
    #     time.sleep(3)

    def edit_success_message(self):
        success_message = "Saved Successfully"
        return success_message
    # return self.driver.edit_employee_success_message
    # return self.driver.dashboard
