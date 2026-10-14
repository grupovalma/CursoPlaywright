Feature: Order Transaction
  Tests related to Order Transactions

    Scenario Outline: Verify Order success message shown in details page
      Given place item order with <username> and <password>
      And the user us on landing page
      When I logging to portal with <username> and <password>
      And navigate to orders page
      And select the orderId
      Then order message is successfully displayed
      Examples:
        | username             | password      |
        | grupovalma@gmail.com | NewPassword01 |


