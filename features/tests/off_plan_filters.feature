
Feature: Test Filters for Off Plan

  @tests
  Scenario: Verify Out of Stocks filter for Off Plan
    Given Open main page
    When Log in to page
    And Click off plan
    Then Verify off plan page opens
    When Filter by Out of Stocks
    Then Verify products have Out of Stock tag