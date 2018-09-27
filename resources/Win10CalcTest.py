"""
Example script for Calculator on Windows 10
Requirements:
  - Windows 10
  - pywinauto 0.6.1+
Win10 version of Calculator is very specific. Few different processes (!)
own different windows and controls, so the full hierarchy can be accessed
through Desktop object only.
Minimized Calculator is a process in a "Suspended" state.
But it can be restored with some trick for invisible main window.
"""
from pywinauto import Desktop, Application, ElementNotFoundError
from VariablesFile import clear_button


class Win10CalcTest:

    app = None
    dlg = None

    def __init__(self):
        self.app = Application(backend="uia").start('calc.exe')
        self.dlg = Desktop(backend="uia").Calculator

    def keyboard_input(self, input_string):
        self.dlg.type_keys(input_string)

    def validate_result(self, expected_string):
        result = self.dlg.child_window(auto_id="CalculatorResults").texts()[0]
        if str(result) == 'Display is ' + expected_string:
            print(f"Result {result} is the expected one!")
        else:
            raise AssertionError(f"Result {result} is different than expected {expected_string}")

    def press_buttons(self, button_name):
        button = self.dlg.child_window(auto_id=button_name+'Button')
        button.click()

    def close_calculator(self):
        close_button = self.dlg.child_window(auto_id='Close')
        close_button.click()
        self.dlg.close()

    def verify_calculator_is_opened(self, expected):
        try:
            if expected:
                return self.dlg.child_window(auto_id="CalculatorResults").wait('visible', 5)
            else:
                return self.dlg.child_window(auto_id="CalculatorResults").wait_not('visible', 5)
        except ElementNotFoundError:
            if expected:
                return False
            else:
                return True


if __name__ == "__main__":
    calc = Win10CalcTest()
    calc.keyboard_input('2*3=')
    calc.validate_result('6')
    calc.press_buttons(clear_button)
    calc.validate_result('0')
    calc.close_calculator()

# dlg.minimize()
# Desktop(backend="uia").window(title='Calculator', visible_only=False).restore()