@StoreEpochTime
Feature: 01 SignUp
  Scenario Outline: Signup with "<credential>" should "<result>"
    Given user navigates to signup page
    When user signs up with "<credential>"
    Then sign up attempt should "<result>"
  Examples:
    | credential | result |
    | valid_signup_credential | pass |
    | repeated_attempt_with_valid_credential | fail |

  Scenario Outline: Signup with "<credential>" should throw "<error>".
    Given user navigates to signup page
    When user signs up with "<credential>"
    Then "<error>" message prevents signup
  Examples:
    | credential | error |
    | all_fields_empty | required_field_error |
    | invalid_email_format | invalid_email_address_error |
    | mismatched_passwords | different_value_error |
    | unsupported_passwords | min_length_error |