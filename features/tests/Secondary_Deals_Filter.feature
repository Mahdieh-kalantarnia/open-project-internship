Feature: Test Scenarios for verify cards


  Scenario: User can filter & verify all cards
     Given Open the main page
     When  Enter username & password
     Then  Click on Continue
     Then  Click on “Secondary” option
     Then  Verify the right page opens
     Then  Click on Filters
     Then  Click want to buy btn
     Then  Click on apply filter btn
     Then  Verify all cards have tag
