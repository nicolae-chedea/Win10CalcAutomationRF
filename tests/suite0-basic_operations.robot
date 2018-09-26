*** Settings ***
Documentation  Verifies basic operations for Windows10 calculator
Library  ../resources/Win10CalcTest.py
Library  Screenshot  screenshot_module=PIL
Test Teardown  run keyword if test failed  Take Screenshot  ${TEST_NAME}
Suite Teardown  user closes calculator

*** Test Cases ***

Type numbers operation and press enter
    user types operation  2*3=
    validate result  6
    user clears calculator
    validate result  0

*** Keywords ***
user closes calculator
    close_calculator

user types operation
    [Arguments]  ${operation}
    keyboard_input  ${operation}

validate result
    [Arguments]  ${expected result}
    validate_result  ${expected_result}

user clears calculator
    press_buttons  ${clear_button}