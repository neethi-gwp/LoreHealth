Feature: 04 Shipping Information
  Scenario Outline: User "<result>" reach order review page with "<shipping_info>" and "<shipping>" shipping method
    Given user has added a random item to cart
    When user proceeds to checkout page
    And user selects "<shipping>" shipping method
    And user fills "<shipping_info>" shipping info
    And user proceeds to order review page
    Then "<error>"  error message is displayed
    And user "<result>" reach order review page
  Examples:
    | shipping | shipping_info | result | error |
    | no | all_required_fields | cannot | shipping_method_not_selected_error |
    | default | all_fields_empty | cannot | required_field_error |
    | default | partially_filled_fields | cannot | required_field_error |
    | default | invalid_email_format | cannot | invalid_email_address_error |
    | default | all_required_fields | can | None |
