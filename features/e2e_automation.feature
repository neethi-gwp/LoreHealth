@StoreEpochTime
Feature: E2E Automation

  Scenario Outline: Sign Up, Login, Add to Cart and Checkout
    Given user navigates to signup page
    When user signs up with "<credential>"
    And user logs out
    And user logs in with "<credential>"
    And user filters products by "<category>"
    And user opens the "<nth>" product
    And user selects size "<size>"
    And user selects color "<color>"
    And user sets item quantity to "<quantity>"
    And user adds item to cart
    And user proceeds to checkout page
    And user selects "<shipping>" shipping method
    And user fills "<shipping_info>" shipping info
    And user proceeds to order review page
    And user places the order
    Then order should be placed successfully

  Examples:
    | credential | category | nth | size | color | quantity | shipping | shipping_info |
    | valid_signup_credential | Women,Tops,Jackets | 2 | M | Blue | 2 | default | all_required_fields |

