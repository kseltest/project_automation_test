from TestUtilities.add_employee_utilities import AddEmployeeActions


class PimAdd:

    def __init__(self):
        pass

    def test_pim_add(self):
        """
        test case to test the user should be able to add new employee in PIM module
        :return:
        """

        #_expected_message = "The user is logged in successfully"
        _expected_message = "Successfully Saved"

        AddEmployeeActions().add_employee()
        assert AddEmployeeActions().add_employee_information() == _expected_message
        print("The user is logged in successfully")

PimAdd().test_pim_add()