from TestUtilities.edit_employee_utilities import EditEmployeeActions


class PimEdit:

    def __init__(self):
        pass

    def test_pim_edit(self):
        """
        test case to test the user should be able to edit exiting employee information in PIM module
        and should see a success message of detail addition
        :return:
        """

        #_expected_message = "The user is logged in successfully"
        _expected_message = "Successfully Saved"

        EditEmployeeActions().login_to_orangehrm()
        assert EditEmployeeActions().employee_information() == _expected_message
        print("The user is logged in successfully")

PimEdit().test_pim_edit()