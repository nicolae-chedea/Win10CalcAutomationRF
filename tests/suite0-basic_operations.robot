*** Settings ***
Documentation  Verifies basic operations for Windows10 calculator
Library  resources/Win10CalcTest.py
Library  Screenshot  screenshot_module=PIL
Variables  resources/VariablesFile.py
Test Teardown  run keyword if test failed  Take Screenshot  ${TEST_NAME}
Suite Teardown  user closes calculator

*** Test Cases ***

Type numbers operation and press enter
    validate calculator is opened  ${True}
    When user types operation  2*3=
    Then user validates result  6
    Given user clears calculator
    Then user validates result  0

*** Keywords ***
user closes calculator
    close_calculator

user types operation
    [Arguments]  ${operation}
    keyboard_input  ${operation}

user validates result
    [Arguments]  ${expected result}
    validate_result  ${expected_result}

user clears calculator
    press_buttons  ${clear_button}

validate calculator is opened
    [Arguments]  ${expected}
    verify_calculator_is_opened  ${expected}
