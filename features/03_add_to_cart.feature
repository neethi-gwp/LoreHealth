Feature: 03 Add to Cart
  Scenario Outline: Add product to Cart
    Given user navigates to home page
    When user filters products by "<category>"
    And user opens the "<nth>" product
    And user selects size "<size>"
    And user selects color "<color>"
    And users sets "<quantity>" and adds item to cart
    Then verify "<item_name>" "<size>" "<color>" "<expected_number_in_cart>" has been added to cart
    And "<message>" is displayed to user
  Examples:
    | category           | item_name       | nth | size | color | quantity | expected_number_in_cart | message |
    | Women,Tops,Jackets | Juno Jacket     | 2   | M    | Blue  | 2        | 2      | success |
    | Gear,Bags          | Driven Backpack |  3  | None |  None | 10000    | 0      | out_of_stock |
    | Gear,Bags          | Driven Backpack |  3  | None | None  | 6000,5000    | 6000      | maximum_limit |