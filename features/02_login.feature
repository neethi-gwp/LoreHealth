Feature: 02 Login
  Scenario Outline: Login with "<credential>" should "<result>"
    Given user navigates to login page
    When user logs in with "<credential>"
    Then log in attempt should "<result>"
  Examples:
    | credential | result |
    | valid_credential | pass |
    | invalid_credential | fail |

  Scenario Outline: Login with "<credential>" throws "<error>"
    Given user navigates to login page
    When user logs in with "<credential>"
    Then "<error>" message prevents login
  Examples:
    | credential | error |
    | all_fields_empty | required_field_error |
    | invalid_email_format | invalid_email_address_error |